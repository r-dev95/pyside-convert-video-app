"""This is the module that defines the main app.
"""

import argparse
import datetime
import math
import sys
from logging import getLogger
from pathlib import Path
from typing import Any, override

from moviepy import VideoFileClip
from pydantic import ValidationError
from PySide6.QtCore import QEvent, QTime, Slot
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (
    QApplication,
    QButtonGroup,
    QFileDialog,
    QListWidgetItem,
    QRadioButton,
    QWidget,
)

from lib.common.decorator import process_time, save_params_log
from lib.common.file import load_yaml
from lib.common.log import SetLogging
from lib.common.process import sec_to_hms
from lib.common.types import (
    FfmpegParams,
    FpathFlag,
    LogLevel,
    LogMsg,
    MsgID,
    ParamLog,
    ThreadID,
    ThreadMsg,
    VideoInfo,
    ZoneInfo,
)
from lib.common.types import ParamKey as K
from lib.components.base import MassageMixin, Worker
from lib.components.ffmpeg import FfmpegWrapper
from lib.components.layout import Ui_Dialog
from lib.components.router import Router
from lib.components.video import VideoPlayer

PARAM_LOG = ParamLog()
LOGGER = getLogger(PARAM_LOG.NAME)


class MainWindow(QWidget, MassageMixin):
    """Defines the main window.

    Args:
        params (dict[str, Any]): parameter.
    """
    thread_id = ThreadID.MAIN

    def __init__(self, params: dict[str, Any], *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.params = params

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.setWindowTitle('Convert Video App')

        self.video_palyer = VideoPlayer(parent=self)
        self.ui.gridLayout.addWidget(self.video_palyer.ui.frame, 0, 1, 1, 1)
        self.ui.gridLayout.setColumnStretch(1, 1)

        self.change_play_file_group = QButtonGroup(parent=self)
        self.change_play_file_group.addButton(self.ui.rbtn_input_file)
        self.change_play_file_group.addButton(self.ui.rbtn_output_file)

        self.resize(1000, 600)

        self.log_bg_color = {
            LogLevel.INFO: '#ffffff',
            LogLevel.ERROR: '#ffff00',
        }

        self.router = Router(parent=self)
        self.threads: dict[str, Worker] = {
            ThreadID.FFMPEG: FfmpegWrapper(parent=self),
            ThreadID.VIDEO: self.video_palyer,
        }

        self.vinfo: VideoInfo = None
        self.input_fpath: Path = None
        self.output_fpath: Path = None

        self.setup()

    @override
    def send_msg(self, to_id: ThreadID, msg_id: MsgID, data: Any) -> None:
        """Send a message to another thread.

        *   It is sent via the :method:`Router.route_msg` method of the :class:`Router`
            Thread class.

        Args:
            to_id (ThreadID): Destination thread ID
            msg_id (MsgID): Message ID.
            data (Any): Data to be sent
        """
        msg = ThreadMsg(
            fm_id=self.thread_id,
            to_id=to_id,
            msg_id=msg_id,
            data=data,
        )
        self.sig_send.emit(msg)

    @override
    def receive_msg(self, msg: ThreadMsg) -> None:
        """Receive a message from another thread.

        *   It is received via the :method:`Router.route_msg` method of the
            :class:`Router` Thread class.

        Args:
            msg (ThreadMsg): Message format class for inter-thread communication.
        """
        match msg.msg_id:
            case MsgID.LOG:
                self.add_log(msg=msg.data)
            case MsgID.FIN_FFMPEG:
                self.finished_ffmpeg()
            case _:
                LOGGER.error(f'Undefined {msg.msg_id=}.')

    @override
    def closeEvent(self, event: QEvent) -> None:  # noqa: N802
        """Stop running threads when the app is closed.
        """
        self.send_msg(to_id=ThreadID.VIDEO, msg_id=MsgID.DEL_THUMBNAIL, data=None)
        self.stop_threads()
        super().closeEvent(event)

    def setup(self) -> None:
        """Set the following.

        *   Connects widget-specific signals and slots.
        *   Connects user-defined signals to slots.
        *   Register threads in the router for inter-thread communication
            (including the main thread).
        """
        self.ui.pbtn_select.clicked.connect(self.select_video_file)
        self.ui.pbtn_run.clicked.connect(self.run)
        self.change_play_file_group.buttonClicked.connect(self.change_play_file)
        self.router.register_thread(tid=self.thread_id, thread=self)
        self.sig_send.connect(self.router.route_msg)
        for tid, thread in self.threads.items():
            self.router.register_thread(tid=tid, thread=thread)
            thread.sig_send.connect(self.router.route_msg)

    @Slot()
    def start_threads(self) -> None:
        """Start the thread.
        """
        if not self.router.isRunning():
            self.router.is_running = True
            self.router.start()
        for thread in self.threads.values():
            if not thread.isRunning():
                thread.is_running = True
                thread.start()

    # @Slot()
    def stop_threads(self) -> None:
        """Stop the thread.
        """
        if self.router.isRunning():
            self.router.is_running = False
            self.router.quit()
            self.router.wait()
        for thread in self.threads.values():
            if thread.isRunning():
                thread.is_running = False
                thread.quit()
                thread.wait()

    def add_log(self, msg: LogMsg) -> None:
        """Add a log.

        Args:
            msg (LogMsg): Log massage format class.
        """
        def _add_item() -> None:
            item = QListWidgetItem(fmted_msg)
            item.setBackground(QColor(self.log_bg_color[msg.level]))
            self.ui.list_widget_log.addItem(item)

        timestamp = datetime.datetime.now(tz=ZoneInfo).strftime('%Y-%m-%d %H:%M:%S')
        if isinstance(msg.data, list):
            for m in msg.data:
                fmted_msg = f'[{timestamp}][{msg.level}][{msg.fm_id}] - {m}'
                _add_item()
        else:
            fmted_msg = f'[{timestamp}][{msg.level}][{msg.fm_id}] - {msg.data}'
            _add_item()

        if self.ui.cbox_auto_scroll.isChecked():
            self.ui.list_widget_log.scrollToBottom()

    def log(self, msg: str, level: LogLevel = LogLevel.INFO) -> None:
        """Add a log for main thread (this class).

        Args:
            msg (str): Log message.
            level (LogLevel): Log level.
        """
        if not isinstance(msg, list):
            msg = [msg]
        msg = LogMsg(fm_id=self.thread_id, data=msg, level=level)
        self.add_log(msg)

    def get_open_fname(self) -> str:
        """Opens a load file selection dialog.

        Returns:
            str: file path.
        """
        fpath, filters = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select video file',
            dir=Path(__file__).parent.absolute().as_posix(),
        )
        LOGGER.debug(f'{fpath=}, {filters=}')
        return fpath

    def get_save_fname(self) -> str:
        """Opens a save file selection dialog.

        Returns:
            str: file path.
        """
        fpath, filters = QFileDialog.getSaveFileName(
            parent=self,
            caption='Select video file',
            dir=self.input_fpath.parent.absolute().as_posix(),
        )
        LOGGER.debug(f'{fpath=}, {filters=}')
        return fpath

    def get_video_info(self, fpath: Path) -> None:
        """Get video information.

        Args:
            fpath (Path): video file path.
        """
        video = VideoFileClip(filename=fpath)
        hh, mm, ss, ms = sec_to_hms(time=video.duration)
        ss = math.ceil(ss + ms)
        self.vinfo = VideoInfo(
            hh=hh,
            mm=mm,
            ss=ss,
            width=video.w,
            height=video.h,
        )
        LOGGER.debug(f'{video.duration=}')
        LOGGER.debug(f'{self.vinfo.hh=}, {self.vinfo.mm=}, {self.vinfo.ss=}')
        LOGGER.debug(f'{self.vinfo.width=}, {self.vinfo.height=}')
        video.close()

    @Slot()
    def select_video_file(self) -> None:
        """Select a load video file.
        """
        fpath = self.get_open_fname()
        if not fpath:
            self.log(msg='ファイルを選択してください。', level=LogLevel.ERROR)
            return

        self.log(msg='ファイルを読み込みました。')
        self.input_fpath = Path(fpath)
        self.get_video_info(fpath=self.input_fpath)

        self.ui.line_input_fpath.setText(fpath)
        time = QTime()
        time.setHMS(self.vinfo.hh, self.vinfo.mm, self.vinfo.ss)
        self.ui.time_video_play.setTime(time)
        self.ui.time_end.setTime(time)
        self.ui.line_video_width.setText(str(self.vinfo.width))
        self.ui.line_video_height.setText(str(self.vinfo.height))
        self.ui.spin_w.setValue(self.vinfo.width)
        self.ui.spin_h.setValue(self.vinfo.height)

        data = FpathFlag.INPUT
        self.video_palyer.input_fpath = self.input_fpath
        self.send_msg(to_id=ThreadID.VIDEO, msg_id=MsgID.CRE_THUMBNAIL, data=data)
        self.send_msg(to_id=ThreadID.VIDEO, msg_id=MsgID.SET_VIDEO, data=fpath)

    @Slot()
    def run(self) -> None:
        """Prepare for video conversion using `ffmpeg` and start each thread.
        """
        if not self.input_fpath:
            self.log(msg='読込ファイルを選択してください。', level=LogLevel.ERROR)
            return

        fpath = self.get_save_fname()
        if not fpath or fpath == self.input_fpath.as_posix():
            msg = [
                '保存ファイルを選択してください。',
                'また読込ファイルと同じディレクトリの時、同じ名前は使えません。',
            ]
            self.log(msg=msg, level=LogLevel.ERROR)
            return

        self.ui.rbtn_output_file.setCheckable(True)
        self.output_fpath = Path(fpath)
        self.ui.line_output_fpath.setText(fpath)

        try:
            params = FfmpegParams(
                input_fpath=self.input_fpath.as_posix(),
                output_fpath=self.output_fpath.as_posix(),
                start_time=self.ui.time_start.text(),
                end_time=self.ui.time_end.text(),
                x=self.ui.spin_x.value(),
                y=self.ui.spin_y.value(),
                width=self.ui.spin_w.value(),
                height=self.ui.spin_h.value(),
            )
            LOGGER.debug(f'{params=}')
        except ValidationError as e:
            for msg in e.errors():
                LOGGER.exception(msg)

        self.send_msg(to_id=ThreadID.FFMPEG, msg_id=MsgID.SET_VINFO, data=self.vinfo)
        self.send_msg(to_id=ThreadID.FFMPEG, msg_id=MsgID.SET_PARAMS, data=params)
        self.start_threads()

    def finished_ffmpeg(self) -> None:
        """Create thumbnails for the converted videos.
        """
        data = FpathFlag.OUTPUT
        self.video_palyer.output_fpath = self.output_fpath
        self.send_msg(to_id=ThreadID.VIDEO, msg_id=MsgID.CRE_THUMBNAIL, data=data)
        self.ui.rbtn_output_file.click()

    @Slot()
    def change_play_file(self, button: QRadioButton) -> None:
        """Change the video file being played.

        Args:
            button (QRadioButton): The class of the selected radio button.
        """
        if button.objectName() == self.ui.rbtn_input_file.objectName():
            video_fpath = self.input_fpath
            thumbnail_flag = FpathFlag.INPUT
        else:
            video_fpath = self.output_fpath
            thumbnail_flag = FpathFlag.OUTPUT

        self.send_msg(to_id=ThreadID.VIDEO, msg_id=MsgID.PAUSE_VIDEO, data=None)
        if video_fpath:
            self.send_msg(
                to_id=ThreadID.VIDEO,
                msg_id=MsgID.SET_VIDEO,
                data=video_fpath,
            )
            self.send_msg(
                to_id=ThreadID.VIDEO,
                msg_id=MsgID.SET_THUMBNAIL,
                data=thumbnail_flag,
            )


@save_params_log(fname=f'log_params_{Path(__file__).stem}.yaml')
@process_time(print_func=LOGGER.info)
def main(params: dict[str, Any]) -> dict[str, Any]:
    """Main.

    This function is decorated by ``@save_params_log`` and ``@process_time``.

    Args:
        params (dict[str, Any]): parameters.

    Returns:
        dict[str, Any]: parameters.
    """
    app = QApplication(sys.argv)
    window = MainWindow(params=params)
    window.show()
    sys.exit(app.exec())
    return params


def set_params() -> dict[str, Any]:
    """Sets the command line arguments and file parameters.

    *   Set only common parameters as command line arguments.
    *   Other necessary parameters are set in the file parameters.
    *   Use a yaml file. (:func:`lib.common.file.load_yaml`)

    Returns:
        dict[str, Any]: parameters.

    .. attention::

        Command line arguments are overridden by file parameters.
        This means that if you want to set everything using file parameters,
        you don't necessarily need to use command line arguments.
    """
    # set the command line arguments.
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
        f'--{K.HANDLER}',
        default=[True, True], type=bool, nargs=2,
        help=(
            f'The log handler flag to use.\n'
            f'True: set handler, False: not set handler\n'
            f'ex) --{K.HANDLER} arg1 arg2 (arg1: stream handler, arg2: file handler)'
        ),
    )
    parser.add_argument(
        f'--{K.LEVEL}',
        default=[20, 20], type=int, nargs=2, choices=[10, 20, 30, 40, 50],
        help=(
            f'The log level.\n'
            f'DEBUG: 10, INFO: 20, WARNING: 30, ERROR: 40, CRITICAL: 50\n'
            f'ex) --{K.LEVEL} arg1 arg2 (arg1: stream handler, arg2: file handler)'
        ),
    )
    parser.add_argument(
        f'--{K.PARAM}',
        default='param/param.yaml', type=str,
        help=('The parameter file path.'),
    )
    parser.add_argument(
        f'--{K.RESULT}',
        default='result', type=str,
        help=('The directory path to save the results.'),
    )

    params = vars(parser.parse_args())

    # set the file parameters.
    if params.get(K.PARAM):
        fpath = Path(params[K.PARAM])
        if fpath.is_file():
            params.update(load_yaml(fpath=fpath))

    return params


if __name__ == '__main__':
    # set the parameters.
    params = set_params()
    # set the logging configuration.
    PARAM_LOG.HANDLER[PARAM_LOG.SH] = params[K.HANDLER][0]
    PARAM_LOG.HANDLER[PARAM_LOG.FH] = params[K.HANDLER][1]
    PARAM_LOG.LEVEL[PARAM_LOG.SH] = params[K.LEVEL][0]
    PARAM_LOG.LEVEL[PARAM_LOG.FH] = params[K.LEVEL][1]
    SetLogging(logger=LOGGER, param=PARAM_LOG)

    if params.get(K.RESULT):
        Path(params[K.RESULT]).mkdir(parents=True, exist_ok=True)

    main(params=params)

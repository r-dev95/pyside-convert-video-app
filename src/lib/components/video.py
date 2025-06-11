"""This is the module that defines the video palyer thread class.
"""

import math
import shutil
import subprocess
import threading
import time
from logging import getLogger
from pathlib import Path
from typing import override

from PySide6.QtCore import QObject, Qt, QTime, QUrl, Slot
from PySide6.QtGui import QPixmap
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import QLabel

from lib.common.process import sec_to_hms
from lib.common.types import (
    FpathFlag,
    LogLevel,
    MsgID,
    ThreadID,
    ThreadMsg,
)
from lib.components.base import Worker
from lib.settings import ParamLog
from lib.ui.video_layout import Ui_Dialog

PARAM_LOG = ParamLog()
LOGGER = getLogger(PARAM_LOG.NAME)


class VideoPlayer(Worker):
    """Define a thread to execute `ffmpeg` commands using `subprocess`.

    Args:
        parent (QObject): Parent QObject class.
    """
    thread_id = ThreadID.VIDEO

    def __init__(self, parent: QObject) -> None:
        super().__init__(parent=parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(parent)

        self.label_thumbnail = QLabel()
        self.label_thumbnail.setStyleSheet('background-color: black;')
        self.widget_video = QVideoWidget()
        self.ui.stacked_widget_video.addWidget(self.label_thumbnail)
        self.ui.stacked_widget_video.addWidget(self.widget_video)
        self.audio_output = QAudioOutput(parent=self, volume=1)
        self.media_player = QMediaPlayer(parent=self)
        self.media_player.setVideoOutput(self.widget_video)
        self.media_player.setAudioOutput(self.audio_output)

        self._input_fpath: Path = None
        self._output_fpath: Path = None
        self.thumbnail_input_fpath: Path = None
        self.thumbnail_output_fpath: Path = None
        self.thumbnail_dpath = Path(__file__).parent / 'thumbnail'
        self.thumbnail_dpath.mkdir(parents=True, exist_ok=True)

        self.setup()

    @property
    def input_fpath(self) -> Path:
        return self._input_fpath

    @input_fpath.setter
    def input_fpath(self, value: Path) -> None:
        if isinstance(value, Path):
            self._input_fpath = value
        else:
            LOGGER.error(f'[input_fpath] must be Path. args: {value=}')

    @property
    def output_fpath(self) -> Path:
        return self._output_fpath

    @output_fpath.setter
    def output_fpath(self, value: Path) -> None:
        if isinstance(value, Path):
            self._output_fpath = value
        else:
            LOGGER.error(f'[output_fpath] must be Path. args: {value=}')

    @override
    def task(self) -> None:
        """No special processing.
        """
        while self._is_running:
            LOGGER.debug(f'{self.thread_id=}({threading.get_ident()}) is running.')
            time.sleep(10)

    @override
    def receive_msg(self, msg: ThreadMsg) -> None:
        """Receive a message from another thread (other than the main thread).

        *   It is received via the :method:`Router.route_msg` method of the
            :class:`Router` Thread class.

        Args:
            msg (ThreadMsg): Message format class for inter-thread communication.
        """
        match msg.msg_id:
            case MsgID.SET_THUMBNAIL:
                if msg.data == FpathFlag.INPUT:
                    fpath = self.thumbnail_input_fpath
                else:
                    fpath = self.thumbnail_output_fpath
                self.set_thumbnail(fpath=fpath)
            case MsgID.CRE_THUMBNAIL:
                if msg.data == FpathFlag.INPUT:
                    in_fpath = self.input_fpath
                    self.thumbnail_input_fpath = (
                        self.thumbnail_dpath / (in_fpath.stem + '_input.png')
                    )
                    out_fpath = self.thumbnail_input_fpath
                else:
                    in_fpath = self._output_fpath
                    self.thumbnail_output_fpath = (
                        self.thumbnail_dpath / (in_fpath.stem + '_output.png')
                    )
                    out_fpath = self.thumbnail_output_fpath
                self.create_thumbnail(input_fpath=in_fpath, output_fpath=out_fpath)
            case MsgID.DEL_THUMBNAIL:
                self.delete_thumbnail()
            case MsgID.SET_VIDEO:
                self.set_play_video(fpath=msg.data)
            case MsgID.PAUSE_VIDEO:
                self.pause_video()
            case _:
                LOGGER.error(f'Undefined {msg.msg_id=}.')

    def setup(self) -> None:
        self.ui.pbtn_play.clicked.connect(self.play_video)
        self.ui.pbtn_pause.clicked.connect(self.pause_video)
        self.ui.slider_play.sliderMoved.connect(self.sync_play_position)
        self.media_player.playbackStateChanged.connect(self.change_stacked_widget)
        self.media_player.positionChanged.connect(self.sync_position)
        self.media_player.durationChanged.connect(self.sync_duration)

    def set_thumbnail(self, fpath: Path) -> None:
        """Set thumbnail to screen.

        Args:
            fpath (Path): thumbnail file path.
        """
        label_size = self.label_thumbnail.size()
        pixmap = QPixmap(fpath)
        pixmap = pixmap.scaled(
            label_size,
            aspectMode=Qt.AspectRatioMode.KeepAspectRatio,
            mode=Qt.TransformationMode.SmoothTransformation,
        )
        self.label_thumbnail.setPixmap(pixmap)

    def create_thumbnail(self, input_fpath: Path, output_fpath: Path) -> None:
        """Create thumbnails.

        Args:
            input_fpath (Path): input file path.
            output_fpath (Path): output file path.
        """
        cmd = [
            'ffmpeg', '-y', '-i', input_fpath,
            '-ss', '00:00:01',
            '-vframes', '1',
            output_fpath,
        ]
        process = subprocess.Popen(
            args=cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True,
        )
        for line in process.stdout:
            msg = line.replace('\n', '')
            self.log(msg=msg)
            LOGGER.info(msg)
        process.wait()

        if process.returncode == 0:
            self.log(msg='サムネイルの作成に成功しました。')
        else:
            self.log(msg='サムネイルの作成に失敗しました。', level=LogLevel.ERROR)

        if output_fpath.exists():
            self.set_thumbnail(fpath=output_fpath)

    def delete_thumbnail(self) -> None:
        """Delete all thumbnails.
        """
        if self.thumbnail_dpath.exists():
            shutil.rmtree(self.thumbnail_dpath)

    def set_play_video(self, fpath: Path) -> None:
        """Set the video to play.

        Args:
            fpath (Path): video file path.
        """
        self.media_player.setSource(QUrl.fromLocalFile(fpath))

    @Slot()
    def change_stacked_widget(self, state: QMediaPlayer.PlaybackState) -> None:
        """Change whether to display thumbnails or videos.

        Args:
            state (QMediaPlayer.PlaybackState): The state of QMediaPlayer.
        """
        match state:
            case QMediaPlayer.PlaybackState.PlayingState:
                self.ui.stacked_widget_video.setCurrentWidget(self.widget_video)
            case QMediaPlayer.PlaybackState.PausedState:
                self.ui.stacked_widget_video.setCurrentWidget(self.widget_video)
            case QMediaPlayer.PlaybackState.StoppedState:
                self.ui.stacked_widget_video.setCurrentWidget(self.label_thumbnail)
            case _:
                LOGGER.error(f'Undefined QMediaPlayer {state=}')

    @Slot()
    def play_video(self) -> None:
        """Play video.
        """
        if not self.media_player.isPlaying():
            self.media_player.play()

    @Slot()
    def pause_video(self) -> None:
        """Pause video.
        """
        if self.media_player.isPlaying():
            self.media_player.pause()

    @Slot()
    def sync_play_position(self, position: int) -> None:
        """Synchronize the video playback position with the slider position.

        Args:
            position (int): Slider position.
        """
        self.media_player.setPosition(position)

    @Slot()
    def sync_position(self, position: int) -> None:
        """Synchronize the slider position with the video playback position.

        Args:
            position (int): The video playback position.
        """
        self.ui.slider_play.setValue(position)

        hh, mm, ss, ms = sec_to_hms(time=position * 0.001)
        ss = math.ceil(ss + ms)
        time = QTime()
        time.setHMS(hh, mm, ss)
        self.ui.time_play.setTime(time)

    @Slot()
    def sync_duration(self, duration: int) -> None:
        """Synchronize the slider range with the video duration.

        Args:
            duration (int): The duration of the video.
        """
        self.ui.slider_play.setRange(0, duration)

        hh, mm, ss, ms = sec_to_hms(time=duration * 0.001)
        ss = math.ceil(ss + ms)
        time = QTime()
        time.setHMS(hh, mm, ss)
        self.ui.time_duration.setTime(time)

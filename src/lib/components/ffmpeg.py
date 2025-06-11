"""This is the module that defines the ffmpeg wrapper thread class.
"""

import subprocess
from logging import getLogger
from typing import override

from PySide6.QtCore import QObject

from lib.common.types import (
    FfmpegParams,
    LogLevel,
    MsgID,
    ThreadID,
    ThreadMsg,
    VideoInfo,
)
from lib.components.base import Worker
from lib.settings import ParamLog

PARAM_LOG = ParamLog()
LOGGER = getLogger(PARAM_LOG.NAME)


class FfmpegWrapper(Worker):
    """Define a thread to execute `ffmpeg` commands using `subprocess`.

    Args:
        parent (QObject): Parent QObject class.
    """
    thread_id = ThreadID.FFMPEG

    def __init__(self, parent: QObject) -> None:
        super().__init__(parent=parent)

        self.vinfo = None
        self.cmd_params = None

    @override
    def task(self) -> None:
        """Run the `ffmpeg` command using `subprocess`.
        """
        if not self.cmd_params:
            LOGGER.error(f'{self.cmd_params=} must set.')
            return

        process = subprocess.Popen(
            args=self.create_command(),
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
            self.log(msg='ビデオの変換に成功しました。')
            self.send_msg(to_id=ThreadID.MAIN, msg_id=MsgID.FIN_FFMPEG, data=None)
        else:
            self.log(msg='ビデオの変換に失敗しました。', level=LogLevel.ERROR)

    @override
    def receive_msg(self, msg: ThreadMsg) -> None:
        """Receive a message from another thread (other than the main thread).

        *   It is received via the :method:`Router.route_msg` method of the
            :class:`Router` Thread class.

        Args:
            msg (ThreadMsg): Message format class for inter-thread communication.
        """
        match msg.msg_id:
            case MsgID.SET_VINFO:
                self.set_video_info(info=msg.data)
            case MsgID.SET_PARAMS:
                self.set_params(params=msg.data)
            case _:
                LOGGER.error(f'Undefined {msg.msg_id=}.')

    def set_video_info(self, info: VideoInfo) -> None:
        """Sets information about the loaded video.

        Args:
            info (VideoInfo): The information about the loaded video.
        """
        self.vinfo = info

    def set_params(self, params: FfmpegParams) -> None:
        """Set parameters when running ffmpeg.

        Args:
            params (FfmpegParams): The parameter for ffmpeg command.
        """
        self.cmd_params = params

    def create_command(self) -> list[str]:
        """Create an `ffmpeg` command.

        Returns:
            list[str]: The command for `subprocess`
        """
        cmd = ['ffmpeg', '-y', '-i', self.cmd_params.input_fpath]

        if self.cmd_params.start_time:
            cmd += ['-ss', self.cmd_params.start_time]

        if self.cmd_params.end_time:
            cmd += ['-to', self.cmd_params.end_time]

        x = self.cmd_params.x
        y = self.cmd_params.y
        w = min(self.vinfo.width - x, self.cmd_params.width)
        h = min(self.vinfo.height - y, self.cmd_params.height)
        if all(isinstance(num, int) for num in [x, y, w, h]):
            cmd += ['-vf', f'crop=w={w}:h={h}:x={x}:y={y}']

        cmd += [self.cmd_params.output_fpath]

        self.log(msg=f'command: {' '.join(cmd)}')
        return cmd

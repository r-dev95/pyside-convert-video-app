"""This is the module that defines the types.
"""

import enum
from typing import Any

from pydantic import BaseModel, Field


class ParamKey(enum.StrEnum):
    """Defines the dictionary key for the main parameters.
    """
    LEVEL = enum.auto()
    PARAM = enum.auto()
    RESULT = enum.auto()
    MODE = enum.auto()
    THEME = enum.auto()


class MsgID(enum.StrEnum):
    """Defines the message ID.
    """
    LOG = enum.auto()
    SET_VINFO = enum.auto()
    SET_PARAMS = enum.auto()
    FIN_FFMPEG = enum.auto()
    SET_THUMBNAIL = enum.auto()
    CRE_THUMBNAIL = enum.auto()
    DEL_THUMBNAIL = enum.auto()
    SET_VIDEO = enum.auto()
    PAUSE_VIDEO = enum.auto()


class ThreadID(enum.StrEnum):
    """Defines the thread ID.
    """
    MAIN = enum.auto()
    ROUTER = enum.auto()
    FFMPEG = enum.auto()
    VIDEO = enum.auto()


class ThreadMsg(BaseModel, validate_assignment=True):
    """Defines a message format for inter-thread communication.
    """
    fm_id: ThreadID
    to_id: ThreadID
    msg_id: MsgID
    data: Any


class LogLevel(enum.StrEnum):
    """Defines the log level.
    """
    INFO = enum.auto()
    ERROR = enum.auto()


class LogMsg(BaseModel, validate_assignment=True):
    """Defines a message format for inter-thread communication.
    """
    fm_id: ThreadID
    data: list[Any]
    level: LogLevel


class VideoInfo(BaseModel, validate_assignment=True):
    """Defines the video information.
    """
    hh: int = Field(ge=0)
    mm: int = Field(ge=0)
    ss: int = Field(ge=0)
    width: int = Field(ge=0)
    height: int = Field(ge=0)


class FfmpegParams(BaseModel, validate_assignment=True):
    """Defines the ffmpeg parameter.
    """
    input_fpath: str
    output_fpath: str
    start_time: str
    end_time: str
    x: int = Field(ge=0)
    y: int = Field(ge=0)
    width: int = Field(ge=0)
    height: int = Field(ge=0)


class FpathFlag(enum.StrEnum):
    INPUT = enum.auto()
    OUTPUT = enum.auto()

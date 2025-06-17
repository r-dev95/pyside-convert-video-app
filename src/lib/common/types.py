"""This is the module that defines the types.
"""

import enum
import zoneinfo
from logging import CRITICAL, DEBUG, ERROR, INFO, WARNING
from typing import Any, ClassVar

from pydantic import BaseModel, Field

#: ZoneInfo class.
ZoneInfo = zoneinfo.ZoneInfo(key='Asia/Tokyo')


class ParamKey(enum.StrEnum):
    """Defines the dictionary key for the main parameters.
    """
    HANDLER = enum.auto()
    LEVEL = enum.auto()
    PARAM = enum.auto()
    RESULT = enum.auto()


class ParamLog(BaseModel):
    """Defines the parameters used in the logging configuration.
    """
    #: str: The stream handler key.
    SH: str = Field(default='sh', frozen=True)
    #: str: The file handler key.
    FH: str = Field(default='fh', frozen=True)
    #: str: The name to pass to ``logging.getLogger``.
    NAME: str = 'main'
    #: ClassVar[dict[str, bool]]: The handler flag to use.
    HANDLER: ClassVar[dict[str, bool]] = {
        SH: True,
        FH: True,
    }
    #: ClassVar[dict[str, int]]: The log level.
    LEVEL: ClassVar[dict[str, int]] = {
        SH: DEBUG,
        FH: DEBUG,
    }
    #: str: The file path.
    FPATH: str = 'log/log.txt'
    #: int: The max file size.
    SIZE: int = Field(default=int(1e+6), gt=0)
    #: int: The number of files.
    NUM: int = Field(default=10, gt=0)

    class Config:
        validate_assignment = True
        extra = 'forbid'


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

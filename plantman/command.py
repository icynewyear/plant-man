from enum import Enum, auto
from dataclasses import dataclass


class CommandType(Enum):
    OPEN = auto()  # sets a switch True
    CLOSE = auto()  # sets a switch False
    TOGGLE = auto()  # toggles a switch
    POLL = auto()  # returns data'attr'
    INFO = auto()  # Returns info for this device
    ADJUST = auto()  # adjusts a 'dial' by data'amount'
    SET = auto()  # sets a 'dial' to data'amount'


SWITCH_CMDS = [CommandType.OPEN, CommandType.CLOSE, CommandType.TOGGLE]
DIAL_CMDS = [CommandType.ADJUST, CommandType.SET]
SENSOR_CMDS = [CommandType.POLL]


@dataclass
class Command:
    uid: str
    cmd_type: CommandType
    data: str = ""

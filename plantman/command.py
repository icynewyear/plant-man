from enum import Enum, auto
from dataclasses import dataclass

class CommandType(Enum):
    OPEN = auto()
    CLOSE = auto()
    TOGGLE = auto()
    
@dataclass
class Command:
    cmd_type: CommandType
    data: str = ""
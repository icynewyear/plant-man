from enum import Enum, auto
from dataclasses import dataclass

class CommandType(Enum):
    OPEN = auto() #sets a switch True
    CLOSE = auto() #sets a switch False
    TOGGLE = auto() #toggles a switch
    POLL = auto() #returns data'attr'
    ADJUST = auto() #adjusts a 'dial' by data'amount'
    SET = auto() #sets a 'dial' to data'amount'
        
    
@dataclass
class Command:
    cmd_type: CommandType
    data: str = ""
from __future__ import annotations
from genericpath import exists
import operator

from plantman.command import Command, CommandType

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from command import Command
    AllowedCommands = list[Command]

class Device(ABC):
    
    name = "Device"
    allowedCommands: AllowedCommands
    switch: bool
    dial: int
    
    
    @abstractmethod
    def connect(self) -> None:
        print(f"{self.name} connected")
        pass
    
    @abstractmethod
    def disconnect(self) -> None:
        print(f"{self.name} disconnected")
        pass
    
    @abstractmethod
    def run_command(self, current_cmd: Command) -> None:
        poll_data = ""
        if current_cmd.cmd_type in self.allowedCommands:
            match current_cmd:
                case Command(cmd_type=CommandType.OPEN):
                    self.switch = True
                case Command(cmd_type=CommandType.CLOSE):
                    self.switch = False
                case Command(cmd_type=CommandType.TOGGLE):
                    self.switch = operator.not_(self.switch) 
                case Command(cmd_type=CommandType.POLL) if hasattr(self, current_cmd.data): 
                    poll_data = getattr(self, current_cmd.data)
                case Command(cmd_type=CommandType.POLL): 
                    poll_data = f"Invalid sensor on {self.name}"
                case Command(cmd_type=CommandType.ADJUST):
                    self.dial += int(current_cmd.data)
                case Command(cmd_type=CommandType.SET):
                    self.dial = int(current_cmd.data)
                
            msg_extra = f' with data: {current_cmd.data}' if current_cmd.data else ''
            print(f"{self.name} running command {current_cmd.cmd_type.name}{msg_extra}")
        else:
            print(f"Command: {current_cmd.cmd_type.name} not allowed on {self.name}")
        if poll_data: print(f"{self.name} response: {poll_data}")
        pass
    
    @abstractmethod
    def status_update(self) -> None: 
        print(f"{self.name} polling.....Status: Active")
        pass
    
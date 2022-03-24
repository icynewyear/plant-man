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
    
    display_name = "Device"
    switch: bool
    dial: int
    allowedCommands: AllowedCommands
    
    @abstractmethod
    def connect(self) -> None:
        if hasattr(self, 'name'):
            self.display_name = self.name
        print(f"{self.display_name} connected")
        pass
    
    @abstractmethod
    def disconnect(self) -> None:
        if hasattr(self, 'name'):
            self.display_name = self.name
        print(f"{self.display_name} disconnected")
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
                case Command(cmd_type=CommandType.POLL):
                    if hasattr(self, current_cmd.data): 
                        poll_data = getattr(self, current_cmd.data)
                    else:
                        poll_data = f"Invalid sensor on {self.display_name}"
                case Command(cmd_type=CommandType.ADJUST):
                    self.dial += int(current_cmd.data)
                case Command(cmd_type=CommandType.SET):
                    self.dial = int(current_cmd.data)


            if hasattr(self, 'name'):
                self.display_name = self.name
                
            msg_extra = f' with data: {current_cmd.data}' if current_cmd.data else ''
            print(f"{self.display_name} running command {current_cmd.cmd_type.name}{msg_extra}")
        else:
            print(f"Command: {current_cmd.cmd_type.name} not allowed on {self.display_name}")
        if poll_data: print(f"Device response: {poll_data}")
        pass
    
    @abstractmethod
    def status_update(self) -> None:
        if hasattr(self, 'name'):
            self.display_name = self.name     
        print(f"{self.display_name} polling.....Status: Active")
        pass
    
from __future__ import annotations
import operator

from plantman.device import Device
from plantman.command import Command, CommandType

from typing import TYPE_CHECKING


class WaterFlowController(Device):
    name: str
    status: bool = False
    
    def __init__(self, name: str = "Water Flow Controller") -> None:
        self.name = name
    
    def connect(self) -> None:
        return super().connect()
    
    def disconnect(self) -> None:
        return super().disconnect()
 
    def run_command(self, command: Command) -> None:
        match command:
            case Command(cmd_type = CommandType.OPEN):
                self.status = True
            case Command(cmd_type = CommandType.CLOSE):
                self.status = False
            case Command(cmd_type = CommandType.TOGGLE):
                self.status = operator.not_(self.status)

        return super().run_command(command)
   
    def status_update(self) -> None:
        super().status_update()
    
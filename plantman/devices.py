from __future__ import annotations
import operator

from plantman.device import Device
from plantman.command import Command, CommandType

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    AllowedCommands = list[Command]


class WaterFlowController(Device):
    name: str
    switch: bool = False
    allowedCommands: AllowedCommands = []
    
    def __init__(self, allowedCommands: AllowedCommands, name: str = "Water Flow Controller", ) -> None:
        self.name = name
        self.allowedCommands: AllowedCommands = allowedCommands
    
    def connect(self) -> None:
        return super().connect()
    
    def disconnect(self) -> None:
        return super().disconnect()
 
    def run_command(self, command: Command) -> None:
        return super().run_command(command)

    def status_update(self) -> None:
        return super().status_update()
        
class Thermometer(Device):
    name: str
    temp_sensor: int = 72
    allowedCommands: AllowedCommands = []
    
    def __init__(self, allowedCommands: AllowedCommands, name: str = "Thermometer", ) -> None:
        self.name = name
        self.allowedCommands = allowedCommands
    
    def connect(self) -> None:
        return super().connect()
    
    def disconnect(self) -> None:
        return super().disconnect()
 
    def run_command(self, command: Command) -> None:
        return super().run_command(command)
   
    def status_update(self) -> None:
        return super().status_update()
    
    
class Thermostat(Device):
    name: str
    dial: int = 60
    allowedCommands: AllowedCommands = []
    
    def __init__(self, allowedCommands: AllowedCommands, name: str="Thermostat", dial: int = 60) -> None:
        self.name = name
        self.allowedCommands = allowedCommands
      
    def connect(self) -> None:
        return super().connect()
    
    def disconnect(self) -> None:
        return super().disconnect()
 
    def run_command(self, command: Command) -> None:
        return super().run_command(command)
   
    def status_update(self) -> None:
        return super().status_update()  
    
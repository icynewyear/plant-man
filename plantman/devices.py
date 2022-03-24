from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    AllowedCommands = list[Command]
    
from plantman.device import Device
from plantman.command import Command, SENSOR_CMDS


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
    """Generic Thermometer Device:
        has a temp_sensor and SENSOR_CMDS by default
        Celsius readings by default

    """
    name: str
    allowedCommands: AllowedCommands = []
    fahrenheit: bool

    def __init__(self, allowedCommands: AllowedCommands = SENSOR_CMDS, name: str = "Thermometer", temp: int = 15, fahrenheit: bool = False) -> None:
        self.name = name
        self.allowedCommands = allowedCommands
        self.temp_sensor = temp
        self.fahrenheit = fahrenheit

    def to_fahrenheit(self):
        return ((self._temp_sensor * 1.8) + 32)

    @property
    def temp_sensor(self):
        if self.fahrenheit:
            return self.to_fahrenheit()
        return self._temp_sensor

    @temp_sensor.setter
    def temp_sensor(self, value):
        self._temp_sensor = value

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

    def __init__(self, allowedCommands: AllowedCommands, name: str = "Thermostat", dial: int = 60) -> None:
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

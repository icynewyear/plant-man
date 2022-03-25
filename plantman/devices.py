from __future__ import annotations
import profile
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    AllowedCommands = list[Command]
    
from plantman.device import Device
from plantman.command import Command, SENSOR_CMDS, SWITCH_CMDS, DIAL_CMDS
from plantman.deviceprofiles import DeviceProfile, SampleValve, SampleThermometer, SampleThermostat


class Valve(Device):
    name: str
    switch: bool = False
    allowedCommands: AllowedCommands = []
    profile: DeviceProfile

    def __init__(self, allowedCommands: AllowedCommands = SWITCH_CMDS, name: str = "Water Flow Controller", profile: DeviceProfile = SampleValve()) -> None:
        self.name = name
        self.allowedCommands: AllowedCommands = allowedCommands
        self.profile = profile

    def connect(self) -> bool:
        return super().connect()

    def disconnect(self) -> bool:
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
    profile: DeviceProfile

    def __init__(self, allowedCommands: AllowedCommands = SENSOR_CMDS, name: str = "Thermometer", temp: int = 15, fahrenheit: bool = False, profile: DeviceProfile = SampleThermometer()) -> None:
        self.name = name
        self.allowedCommands = allowedCommands
        self.temp_sensor = temp
        self.fahrenheit = fahrenheit
        self.profile = profile

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

    def connect(self) -> bool:
        return super().connect()

    def disconnect(self) -> bool:
        return super().disconnect()

    def run_command(self, command: Command) -> None:
        return super().run_command(command)

    def status_update(self) -> None:
        return super().status_update()


class Thermostat(Device):
    name: str
    dial: int = 60
    allowedCommands: AllowedCommands = []
    profile: DeviceProfile

    def __init__(self, allowedCommands: AllowedCommands = DIAL_CMDS, name: str = "Thermostat", dial: int = 60, profile: DeviceProfile = SampleThermostat()) -> None:
        self.name = name
        self.allowedCommands = allowedCommands
        self.profile = profile

    def connect(self) -> bool:
        return super().connect()

    def disconnect(self) -> bool:
        return super().disconnect()

    def run_command(self, command: Command) -> None:
        return super().run_command(command)

    def status_update(self) -> None:
        return super().status_update()

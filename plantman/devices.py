from __future__ import annotations
import profile
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    AllowedCommands = list[Command]

from .device import Device
from .command import Command, SENSOR_CMDS, SWITCH_CMDS, DIAL_CMDS
from .deviceprofiles import DeviceProfile, SampleValve, SampleThermometer, SampleThermostat


class Valve(Device):
    """Generic Valve Device:
        has a switch and SWITCH_CMDS by default
    """

    def __init__(self, allowedCommands: AllowedCommands = SWITCH_CMDS, name: str = "Valves", profile: DeviceProfile = SampleValve()) -> None:
        self.name = name
        self.switch = True  # TODO: poll device for starting state
        self.allowedCommands: AllowedCommands = allowedCommands
        self.profile = profile

    def connect(self) -> bool:
        return super().connect()

    def disconnect(self) -> bool:
        return super().disconnect()

    def run_command(self, command: Command) -> bool:
        return super().run_command(command)

    def status_update(self) -> None:
        return super().status_update()


class Thermometer(Device):
    """Generic Thermometer Device:
        has a temp_sensor and SENSOR_CMDS by default
        Celsius readings by default
    """

    def __init__(self, allowedCommands: AllowedCommands = SENSOR_CMDS, name: str = "Thermometer", temp: int = 15, fahrenheit: bool = False, profile: DeviceProfile = SampleThermometer()) -> None:
        self.name = name
        self.temp_sensor = temp  # TODO: poll device for starting state
        self.fahrenheit = fahrenheit
        self.allowedCommands = allowedCommands
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

    def run_command(self, command: Command) -> bool:
        return super().run_command(command)

    def status_update(self) -> None:
        return super().status_update()


class Thermostat(Device):
    """Generic Thermostat Device:
        has a dial and DIAL_CMDS by default
    """

    def __init__(self, allowedCommands: AllowedCommands = DIAL_CMDS, name: str = "Thermostat", dial: int = 60, profile: DeviceProfile = SampleThermostat()) -> None:
        self.name = name
        self.dial = dial  # TODO: poll device for starting state
        self.allowedCommands = allowedCommands
        self.profile = profile

    def connect(self) -> bool:
        return super().connect()

    def disconnect(self) -> bool:
        return super().disconnect()

    def run_command(self, command: Command) -> bool:
        return super().run_command(command)

    def status_update(self) -> None:
        return super().status_update()

from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    AllowedCommands = list[Command]
    from plantman.deviceprofiles import DeviceProfile

import operator
from abc import ABC, abstractmethod

from plantman.error import DeviceCommandFailedError
from plantman.command import Command, CommandType


class Device(ABC):
    """Abstract class for generic device function
        provides basic command handling and hooks for DeviceProfile command handling 
    """
    @abstractmethod
    def connect(self) -> bool:
        if self.profile.connect():
            print(f"{self.name} connected")
            return True
        else:
            print(f"{self.name} failed to connect.")
            return False

    @abstractmethod
    def disconnect(self) -> bool:
        if self.profile.disconnect():
            print(f"{self.name} disconnected")
            return True
        else:
            print(f"{self.name} failed to disconnect.")
            return False

    @abstractmethod
    def run_command(self, current_cmd: Command) -> bool:
        poll_data = ""
        result = False
        if current_cmd.cmd_type not in self.allowedCommands:
            print(
                f"Command: {current_cmd.cmd_type.name} not allowed on {self.name}")
            return False
        match current_cmd:
            # Switch commands
            case Command(cmd_type=CommandType.OPEN):
                if self.profile.open():
                    self.switch = True
                else:
                    raise DeviceCommandFailedError(current_cmd)
            case Command(cmd_type=CommandType.CLOSE):
                if self.profile.close():
                    self.switch = False
                else:
                    raise DeviceCommandFailedError(current_cmd)

            case Command(cmd_type=CommandType.TOGGLE):
                if self.profile.toggle():
                    self.switch = operator.not_(self.switch)
                else:
                    raise DeviceCommandFailedError(current_cmd)
            # Dial Commands
            case Command(cmd_type=CommandType.ADJUST):
                if self.profile.adjust():
                    self.dial += int(current_cmd.data)
                else:
                    raise DeviceCommandFailedError(current_cmd)
            case Command(cmd_type=CommandType.SET):
                if self.profile.set():
                    self.dial = int(current_cmd.data)
                else:
                    raise DeviceCommandFailedError(current_cmd)
            # Sensor Commands
            case Command(cmd_type=CommandType.POLL) if hasattr(self, current_cmd.data):
                if self.profile.poll():
                    poll_data = getattr(self, current_cmd.data)
                else:
                    raise DeviceCommandFailedError(current_cmd)
            case Command(cmd_type=CommandType.POLL):
                poll_data = f"Invalid sensor on {self.name}"

        msg_extra = f' with data: {current_cmd.data}' if current_cmd.data else ''
        print(
            f"{self.name} running command {current_cmd.cmd_type.name}{msg_extra}")
        if poll_data:
            print(f"{self.name} response: {poll_data}")
        return result

    @abstractmethod
    def status_update(self) -> None:
        print(f"{self.name} polling.....Status: Active")
        pass

    # @abstractmethod
    # def get_info(self, data: str) -> None:
    #     pass

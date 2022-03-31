from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .command import Command


class DeviceError(Exception):
    """base error for device module. 
    """
    pass


class DeviceConnectFailedError(DeviceError):
    """raiseed when a device fails to connect
    """

    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"{self.name} failed to connect."
    
class DeviceDisconnectFailedError(DeviceError):
    """raiseed when a device fails to connect
    """

    def __init__(self, uid: str) -> None:
        self.uid = uid

    def __str__(self) -> str:
        return f"{self.uid} failed to disconnect."       


class DeviceCommandFailedError(DeviceError):
    """Raised when a device reports a failure to perform a command
    """

    def __init__(self, cmd: Command) -> None:
        self.cmd = cmd

    def __str__(self) -> str:
        return f"{self.cmd.uid} failed to perform {self.cmd.cmd_type.name}"
class DeviceOperationNotAllowedError(DeviceError):
    """Raised when a device does not suport an operation
    """

    def __init__(self, cmd: Command) -> None:
        self.cmd = cmd

    def __str__(self) -> str:
        return f"{self.cmd.uid} cannot perform {self.cmd.cmd_type.name}"

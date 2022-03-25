import random
import string

from plantman.device import Device
from plantman.error import DeviceConnectFailedError, DeviceDisconnectFailedError



def generate_uid(len: int = 12) -> str:
    return "".join(random.choices(string.ascii_uppercase, k=len))


class DeviceManager:
    """class to handle loading, unloading, and running commands on devices"""

    def __init__(self):
        self.devices: dict[str, Device] = {}

    def register_device(self, device: Device) -> str:
        """takes in a device, runs device connect, and assigns a uid

        Returns:
            str: uid for device
        """
        if device.connect():
            while True:
                new_uid = generate_uid()
                if new_uid not in self.devices.keys():
                    break
            self.devices[new_uid] = device
            return new_uid
        else:
            raise DeviceConnectFailedError(device.name)
            return "CONNECT FAILURE"

    def unregister_device(self, uid: str) -> bool:
        """runs a devices disconnect and removes it from 
            this device manager's device list

        Args:
            uid (str): uid of the device to unregister

        Returns:
            bool: success/failure
        """
        if self.devices[uid].disconnect():
            del self.devices[uid]
            return True
        else:
            raise DeviceDisconnectFailedError(uid)
            return False

    def get_device(self, uid: str) -> Device:
        """returns the device of specified uid

        Args:
            uid (str): uid of requested device

        Returns:
            Device: requested device
        """
        return self.devices[uid]

    def run_commands(self, program) -> None:
        for command in program:
            self.devices[command.uid].run_command(command)
        pass

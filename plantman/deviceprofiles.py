import logging
from abc import ABC, abstractmethod

##TODO Add custom exception

class DeviceProfile(ABC):
    """Abstract class for DeviceProfiles
        Subclasses should define device specific functionality for each potential function
        all functions should return True on success and False on failure
        Functions unaval to this device should raise Exception
    """
    @abstractmethod
    def connect(self) -> bool:
        pass

    @abstractmethod
    def disconnect(self) -> bool:
        pass

    @abstractmethod
    def open(self) -> bool:
        pass

    @abstractmethod
    def close(self) -> bool:
        pass

    @abstractmethod
    def toggle(self) -> bool:
        pass

    @abstractmethod
    def poll(self) -> bool:
        pass

    @abstractmethod
    def adjust(self) -> bool:
        pass

    @abstractmethod
    def set(self) -> bool:
        pass


class SampleValve(DeviceProfile):
    """A basic dummy valve profile implementation"""
    def connect(self) -> bool:
        logging.info("Valve connected")
        return True

    def disconnect(self) -> bool:
        logging.info("Valve disconnected")
        return True

    def open(self):
        logging.info("Valve Open")
        return True

    def close(self):
        logging.info("Valve Closed")
        return True

    def toggle(self):
        logging.info("Valve Toggled")
        return True

    def poll(self):
        logging.info("Valve State Polled")
        return True

    def adjust(self):
        logging.warning("Unimplimented device behaviour")
        return False

    def set(self):
        logging.warning("Unimplimented device behaviour")
        return False


class SampleThermostat(DeviceProfile):
    """A basic dummy thermostat profile implementation"""
    def connect(self) -> bool:
        logging.info("Thermostat connected")
        return True

    def disconnect(self) -> bool:
        logging.info("Thermostat disconnected")
        return True

    def open(self):
        logging.warning("Unimplimented device behaviour")
        return False

    def close(self):
        logging.warning("Unimplimented device behaviour")
        return False

    def toggle(self):
        logging.warning("Unimplimented device behaviour")
        return False

    def poll(self):
        logging.info("Thermostat State Polled")
        return True

    def adjust(self):
        logging.info("Thermostat adjusted")
        return True

    def set(self):
        logging.info("Thermostat set")
        return True


class SampleThermometer(DeviceProfile):
    """A basic dummy thermometer profile implementation"""
    def connect(self) -> bool:
        logging.info("Thermometer connected")
        return True

    def disconnect(self) -> bool:
        logging.info("Thermometer disconnected")
        return True

    def open(self):
        logging.warning("Unimplimented device behaviour")
        return False

    def close(self):
        logging.warning("Unimplimented device behaviour")
        return False

    def toggle(self):
        logging.warning("Unimplimented device behaviour")
        return False

    def poll(self):
        logging.info("Thermometer State Polled")
        return True

    def adjust(self):
        logging.warning("Unimplimented device behaviour")
        return False

    def set(self):
        logging.warning("Unimplimented device behaviour")
        return False

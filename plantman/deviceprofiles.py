import logging
from abc import ABC, abstractmethod


class DeviceProfile(ABC):

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
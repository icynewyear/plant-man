from __future__ import annotations


from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from command import Command
    

class Device(ABC):
    
    displayName = "Device"
    
    @abstractmethod
    def connect(self) -> None:
        if hasattr(self, 'name'):
            self.displayName = self.name
        print(f"{self.displayName} connected")
        pass
    
    @abstractmethod
    def disconnect(self) -> None:
        if hasattr(self, 'name'):
            self.displayName = self.name
        print(f"{self.displayName} disconnected")
        pass
    
    @abstractmethod
    def run_command(self, command: Command) -> None:
        if hasattr(self, 'name'):
            self.displayName = self.name
            
        msg_extra = f' with data: {command.data}' if command.data else ''
        print(f"{self.displayName} running {command.cmd_type.name}{msg_extra}")
        pass
    
    @abstractmethod
    def status_update(self) -> None:
        if hasattr(self, 'name'):
            self.displayName = self.name     
        print(f"{self.displayName} polling.....\nStatus: {self.status if hasattr(self, 'status') else 'Undefined'}")
        pass
    
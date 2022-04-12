

from calendar import day_abbr
from dataclasses import dataclass
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .manager import DeviceManager
from dataclasses import dataclass

from .utils import generate_uid

@dataclass
class Plot():
    uid: str
    device_manager: DeviceManager
    
class PlotManager():
    """docstring for PlotManager."""
    def __init__(self,):
        self.plots: dict[str, Plot] = {}
        
    def register_plot(self, plot: Plot) -> str:
        """registers a new plot, assigns a uid

        Args:
            plot (Plot): plot to register to this manager

        Returns:
            str: uid of registered plot
        """
        while True:
            new_uid = generate_uid()
            if new_uid not in self.plots.keys():
                break
        self.plots[new_uid] = plot
        return new_uid       
    
    def unregister_plot(self, uid: str) -> None:
        self.plots = [p for p in self.plots if p != uid]
    
    def run_program(self,):
        pass
    
    
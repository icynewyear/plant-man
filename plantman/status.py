from enum import Enum, auto
from dataclasses import dataclass


@dataclass
class Status:
    data: str = ""
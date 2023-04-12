"""
create dataclass `Engine`
"""
from dataclasses import dataclass


@dataclass
class Engine:
    volume: float
    pistons: int


Engine_1 = Engine(3.4, 1)

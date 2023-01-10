from os import path
from dataclasses import dataclass
import math
import re


@dataclass
class Monkey:
    items: list[int]
    op: str
    div_by: int
    targets: tuple[int, int]


def ints(string):
    return list(map(int, re.findall(r"-?[0-9]+", string)))
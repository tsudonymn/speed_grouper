from dataclasses import dataclass
from typing import Tuple, List

from person import Person


@dataclass
class Round:
    number: int
    groups: List[Tuple[Person]]

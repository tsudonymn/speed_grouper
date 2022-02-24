from dataclasses import dataclass
from typing import List


@dataclass
class Person:
    name: str


def generate_person_list(num_people: int) -> List[Person]:
    num_strs = map(str, range(1, num_people + 1))
    all_the_people = list(map(lambda p: Person(f"Person{p}"), num_strs))
    return all_the_people



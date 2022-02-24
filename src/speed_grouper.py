from typing import List, Tuple

import grouper
from grouper import get_combinations_for
from person import Person
from round import Round


class SpeedGrouper:
    def __init__(self, people: List[Person],
                 people_per_group: int = 3):
        self.people: List[Person] = people
        self.people_per_group = people_per_group
        self.rounds: List[Round] = []
        self.remaining_combinations: List[Tuple[Person, ...]] = get_combinations_for(self.people, self.people_per_group)

    def build_next_round(self):
        groups_for_round = []
        for person in self.people:
            if not grouper.is_in_a_group_already(person, groups_for_round):
                next_group_for_person = grouper.find_next_group_for(person, self.remaining_combinations)
                groups_for_round.append(next_group_for_person)
        the_round = Round(self.get_round_number(), groups_for_round)
        self.rounds.append(the_round)
        return the_round

    def get_round_number(self):
        return len(self.rounds) + 1

from typing import List, Tuple

from grouper import get_combinations_for, is_in_a_group_already, flatten_to_set, find_next_group, \
    group_contains_any_of_these_people
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
            if not is_in_a_group_already(person, groups_for_round):
                next_group_for_person = self.get_group_for_person_from_remaining(person, groups_for_round)
                groups_for_round.append(next_group_for_person)
        the_round = Round(self.get_round_number(), groups_for_round)
        self.rounds.append(the_round)
        return the_round

    def get_group_for_person_from_remaining(self, person, current_groups: List[Tuple[Person, ...]]):
        people_already_in_groups = flatten_to_set(current_groups)
        filter(lambda a_group: group_contains_any_of_these_people(people_already_in_groups, a_group),
               self.remaining_combinations)
        group = find_next_group(person, self.remaining_combinations)
        self.remaining_combinations.remove(group)
        return group

    def get_round_number(self):
        return len(self.rounds) + 1

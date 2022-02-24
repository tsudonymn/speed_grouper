from itertools import combinations
from pprint import pprint

from typing import List, Tuple

from person import generate_person_list, Person

DEFAULT_GROUP_SIZE = 3


def form_groups(people: List[str], people_per_group=DEFAULT_GROUP_SIZE):
    all_combos = get_combinations_for(people, people_per_group)
    combos_for_person = group_by_person(people, all_combos)
    return combos_for_person


def group_by_person(people: List[Person], combos):
    by_person = {}
    for p in people:
        combos_for_person = list(filter(lambda c: c[0].name == p.name, combos))
        by_person[p.name] = combos_for_person
    return by_person


def get_combinations_for(people: List[Person], people_per_group=DEFAULT_GROUP_SIZE):
    p = combinations(people, people_per_group)
    return list(p)


def person_in_group(person, group):
    return person in group


def is_in_a_group_already(person, groups):
    for g in groups:
        if person in g:
            return True
    return False


def get_next_group(chosen_groups_this_round: List[Tuple[str, str, str]],
                   groups_to_search: List[Tuple[str, str, str]]) \
        -> List[Tuple[str, str, str]]:
    for suggested_grouping in groups_to_search:
        if len(groups_to_search) == 0:
            return None
        for person in suggested_grouping:
            if not is_in_a_group_already(person, chosen_groups_this_round):
                return suggested_grouping


def get_next_round(last_round_groups: List[Tuple[str, str, str]],
                   remaining_groups: List[Tuple[str, str, str]],
                   num_groups) -> List[Tuple[str, str, str]]:
    all_chosen_groups = last_round_groups.copy()
    next_round_groups = []
    for group in remaining_groups:
        if len(next_round_groups) >= num_groups:
            return next_round_groups
        next_group = get_next_group(all_chosen_groups, remaining_groups)
        if next_group is not None:
            next_round_groups.append(next_group)
            all_chosen_groups.append(next_group)

    return next_round_groups


def suggest_rounds(list_of_people, people_per_group=DEFAULT_GROUP_SIZE):
    number_of_groups = len(list_of_people) / people_per_group
    all_combos = get_combinations_for(list_of_people, people_per_group)

    first_round = get_next_round([], all_combos, number_of_groups)
    print_groups(first_round)

    round2 = get_next_round(first_round, all_combos, number_of_groups)
    print_groups(round2)


def print_groups(the_groups):
    print("Groups: ")
    for g in the_groups:
        print(g)


def number_of_groups_for_number_of_people(number_of_people, people_per_group):
    return number_of_people / people_per_group


if __name__ == '__main__':
    num_people = 15  # int(input("How many people?: "))

    all_the_people = generate_person_list(num_people)
    print("People:")
    pprint(all_the_people)

    suggest_rounds(all_the_people)
    # groups = form_groups(all_the_people)
    # combos = get_combinations_for(all_the_people, 3)
    # print_groups(combos)
    # range
    # print_groups(attendees)


def find_next_group_for(person, remaining_group_combos: List[Tuple[Person, ...]]):
    return next(filter(lambda group: person in group, remaining_group_combos))

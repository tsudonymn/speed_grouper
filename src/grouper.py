from itertools import combinations, chain
from pprint import pprint

from typing import List, Tuple, Set

from person import generate_person_list, Person

DEFAULT_GROUP_SIZE = 3


def group_contains_any_of_these_people(people_already_in_groups: Set[Person], a_group):
    return len(people_already_in_groups.intersection(a_group)) > 0


def flatten_to_set(groups: List[Tuple[Person, ...]]):
    return set(chain(*groups))


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


def find_next_group(person, remaining_group_combos: List[Tuple[Person, ...]]):
    try:
        result = next(filter(lambda group: person in group, remaining_group_combos))
    except StopIteration:
        result = {}
    return result

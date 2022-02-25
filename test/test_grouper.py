from itertools import combinations, chain
from unittest import TestCase

from assertpy import assert_that

from grouper import get_combinations_for, person_in_group, number_of_groups_for_number_of_people, find_next_group, \
    flatten_to_set, group_contains_any_of_these_people
from person import Person


class Test(TestCase):

    def test_group_contains_any_of_these_people(self):
        p1 = Person('1')
        p2 = Person('2')
        p3 = Person('3')
        p4 = Person('4')
        p5 = Person('5')
        g1 = (p1, p2, p3)
        a_group123 = g1

        group12 = {p1, p2}
        group45 = {p4, p5}
        assert_that(group_contains_any_of_these_people(group12, a_group123)).is_true()
        assert_that(group_contains_any_of_these_people(group45, a_group123)).is_false()

    def test_find_next_group_for(self):
        p1 = Person('1')
        p2 = Person('2')
        p3 = Person('3')
        p4 = Person('4')
        p5 = Person('5')
        p6 = Person('6')
        g1 = (p1, p2, p3)
        g2 = (p4, p5, p6)
        remaining_groups = [g1, g2]
        expected = g2

        assert_that(find_next_group(p4, remaining_groups)).is_equal_to(expected)

    def test_number_of_groups_for_number_of_people(self):
        num_people = 15
        people_per_group = 3
        result = number_of_groups_for_number_of_people(num_people, people_per_group)
        assert_that(result).is_equal_to(5)

    def test_get_combinations_for(self):
        nums = [1, 2, 3, 4, 5, 6]
        people = [Person(str(x)) for x in nums]

        expected = list(combinations(people, 3))
        groups = get_combinations_for(people)
        assert_that(groups).is_equal_to(expected)

    def test_person_in_group(self):
        groups = [('1', '2', '3'), ('1', '2', '4')]
        in_person = '1'
        out_person = '9'

        assert_that(person_in_group(in_person, groups[0])).is_true()
        assert_that(person_in_group(out_person, groups[0])).is_false()

    def test_flatten(self):
        p1 = Person('1')
        p2 = Person('2')
        p3 = Person('3')
        p4 = Person('4')
        p5 = Person('5')
        p6 = Person('6')
        g1 = (p1, p2, p3)
        g2 = (p4, p5, p6)
        groups = [g1, g2]
        expected = {p1, p2, p3, p4, p5, p6}
        result = flatten_to_set(groups)
        assert_that(result).is_equal_to(expected)

from itertools import combinations
from unittest import TestCase

from assertpy import assert_that

from grouper import get_combinations_for, group_by_person, person_in_group, get_next_group, \
    generate_person_list, get_next_round, number_of_groups_for_number_of_people, find_next_group_for
from person import Person
from speed_grouper import SpeedGrouper


class Test(TestCase):
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
        expected = (g2)

        assert_that(find_next_group_for(p4, remaining_groups)).is_equal_to(expected)

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

    def test_group_by(self):
        expected1 = [('1', '2', '3'), ('1', '2', '4'), ('1', '2', '5'), ('1', '2', '6'), ('1', '3', '4'),
                     ('1', '3', '5'), ('1', '3', '6'), ('1', '4', '5'), ('1', '4', '6'), ('1', '5', '6')]
        nums = [1, 2, 3, 4, 5, 6]
        people = [Person(str(x)) for x in nums]

        groups = get_combinations_for(people)

        result = group_by_person(people, groups)
        assert_that(result[people[0].name]).is_equal_to(expected1)
        assert_that(result['4']).is_equal_to([('4', '5', '6')])

    def test_in_group(self):
        groups = [('1', '2', '3'), ('1', '2', '4')]
        in_person = '1'
        out_person = '9'

        assert_that(person_in_group(in_person, groups[0])).is_true()
        assert_that(person_in_group(out_person, groups[0])).is_false()

    def test_next_group(self):
        expected = ('7', '5', '6')

        chosen_groups = [('1', '2', '3'), ('1', '2', '4')]
        remaining_groups = [('4', '5', '6'), expected]
        grouper = SpeedGrouper(chosen_groups, remaining_groups)
        grouper.next_group()

        chosen_expected = [('1', '2', '3'), ('1', '2', '4')]
        remain_expected = []

        result = get_next_group(chosen_groups, remaining_groups)
        assert_that(result).is_equal_to(expected)
        assert_that(chosen_groups).is_equal_to(chosen_expected)
        assert_that(result).is_equal_to(remain_expected)

    def test_first_group(self):
        chosen_groups = []
        expected = ('1', '5', '6')
        remaining_groups = [expected, ('4', '5', '6')]
        result = get_next_group(chosen_groups, remaining_groups)
        assert_that(result).is_equal_to(expected)

    def test_get_next_round(self):
        all_the_people = generate_person_list(15)
        all_combos = get_combinations_for(all_the_people)

        expected = [('Person1', 'Person2', 'Person3'), ('Person4', 'Person5', 'Person6'),
                    ('Person7', 'Person8', 'Person9')]
        num_groups = 3
        first_round_groups = get_next_round([], all_combos, num_groups)
        assert_that(len(first_round_groups)).is_equal_to(num_groups)
        assert_that(first_round_groups).is_equal_to(expected)

        expected2 = []
        round2 = get_next_round(first_round_groups, all_combos, num_groups)
        assert_that(len(round2)).is_equal_to(num_groups)
        assert_that(round2).is_equal_to(expected2)

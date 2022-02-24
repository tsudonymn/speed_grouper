from unittest import TestCase

from assertpy import assert_that

from grouper import generate_person_list
from speed_grouper import SpeedGrouper


class Test(TestCase):
    def test_get_next_round(self):
        all_the_people = generate_person_list(15)

        num_per_group = 3
        groups_per_round = len(all_the_people) / num_per_group
        grouper = SpeedGrouper(all_the_people, num_per_group)

        round1_expected_groups = [('Person1', 'Person2', 'Person3'), ('Person4', 'Person5', 'Person6'),
                                  ('Person7', 'Person8', 'Person9')]
        round = grouper.build_next_round()
        assert_that(round.number).is_equal_to(1)
        assert_that(len(grouper.rounds)).is_equal_to(1)
        assert_that(len(round.groups)).is_equal_to(groups_per_round)
        # assert_that(round.groups).is_equal_to(round1_expected_groups)
        #
        # expected2 = []
        # round2 = grouper.build_next_round()
        # assert_that(len(round2)).is_equal_to(num_per_group)
        # assert_that(round2).is_equal_to(expected2)

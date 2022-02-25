from unittest import TestCase

from assertpy import assert_that

from grouper import generate_person_list
from person import Person
from speed_grouper import SpeedGrouper


class Test(TestCase):
    def test_get_next_round(self):
        all_the_people = generate_person_list(15)

        num_per_group = 3
        groups_per_round = len(all_the_people) / num_per_group
        grouper = SpeedGrouper(all_the_people, num_per_group)

        p1 = Person('1')
        p2 = Person('2')
        p3 = Person('3')
        p4 = Person('4')
        p5 = Person('5')
        p6 = Person('6')
        p7 = Person('7')
        p8 = Person('8')
        p9 = Person('9')
        p10 = Person('10')
        p11 = Person('11')
        p12 = Person('12')
        p13 = Person('13')
        p14 = Person('14')
        p15 = Person('15')
        g123 = (p1, p2, p3)
        g456 = (p4, p5, p6)
        g789 = (p7, p8, p9)
        g101112 = (p10, p11, p12)
        g131415 = (p13, p14, p15)
        round1_expected_groups = [g123, g456, g789, g101112, g131415 ]
        round = grouper.build_next_round()
        assert_that(round.number).is_equal_to(1)
        assert_that(len(grouper.rounds)).is_equal_to(1)
        assert_that(len(round.groups)).is_equal_to(groups_per_round)
        assert_that(len(round.groups)).is_equal_to(len(round1_expected_groups))
        # assert_that(round.groups).is_equal_to(round1_expected_groups)
        assert_that(set(round.groups).intersection(set(round1_expected_groups))).is_equal_to(set())
        #
        # expected2 = []
        # round2 = grouper.build_next_round()
        # assert_that(len(round2)).is_equal_to(num_per_group)
        # assert_that(round2).is_equal_to(expected2)

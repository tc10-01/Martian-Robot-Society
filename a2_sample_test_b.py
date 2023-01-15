"""CSC148 Assignment 1: Sample tests

=== CSC148 Winter 2022 ===
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains sample tests for Assignment 2.

Warning: This is an extremely incomplete set of tests! Add your own tests
to be confident that your code is correct.

Note: this file is to only help you; you will not submit it when you hand in
the assignment.

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) University of Toronto
"""
# Note that some tests under each Task subheading depend on other methods
# implemented within that task, and previous tasks before it

from society_hierarchy import *


def sample_society0() -> Society:
    """Return a Society of sufficient complexity without District Leaders.
    """
    s = Society()
    c1 = Citizen(1, 'Citizen 1', 3001, 'Watcher', 10)
    s.add_citizen(c1)
    c2 = Citizen(2, 'Citizen 2', 3002, 'Bank robber', 19)
    c3 = Citizen(3, 'Citizen 3', 3003, 'Cook', 82)
    c4 = Citizen(4, 'Citizen 4', 3004, 'Cook', 5)
    s.add_citizen(c2, 1)
    s.add_citizen(c3, 1)
    s.add_citizen(c4, 1)
    c5 = Citizen(5, 'Citizen 5', 3005, 'Farmer', 101)
    c6 = Citizen(6, 'Citizen 6', 3006, 'Coach', 56)
    s.add_citizen(c5, 2)
    s.add_citizen(c6, 2)
    c8 = Citizen(8, 'Citizen 8', 3008, 'Farmer', 22)
    c9 = Citizen(9, 'Citizen 9', 3009, 'Farmer', 22)
    c10 = Citizen(10, 'Citizen 10', 3010, 'Driver', 22)
    s.add_citizen(c8, 6)
    s.add_citizen(c9, 6)
    s.add_citizen(c10, 6)
    c7 = Citizen(7, 'Citizen 7', 3007, 'Builder', 58)
    s.add_citizen(c7, 4)
    return s


def sample_society1() -> Society:
    """Return a Society of sufficient complexity with District leaders.
    """
    s = Society()
    c1 = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    s.add_citizen(c1)
    c2 = DistrictLeader(2, 'Citizen 2', 3002, 'Bank robber', 19, 'D2')
    c3 = Citizen(3, 'Citizen 3', 3003, 'Cook', 82)
    c4 = Citizen(4, 'Citizen 4', 3004, 'Cook', 5)
    s.add_citizen(c2, 1)
    s.add_citizen(c3, 1)
    s.add_citizen(c4, 1)
    c5 = Citizen(5, 'Citizen 5', 3005, 'Farmer', 101)
    c6 = Citizen(6, 'Citizen 6', 3006, 'Coach', 56)
    s.add_citizen(c5, 2)
    s.add_citizen(c6, 2)
    c8 = Citizen(8, 'Citizen 8', 3008, 'Farmer', 22)
    c9 = Citizen(9, 'Citizen 9', 3009, 'Farmer', 22)
    c10 = Citizen(10, 'Citizen 10', 3010, 'Driver', 22)
    s.add_citizen(c8, 6)
    s.add_citizen(c9, 6)
    s.add_citizen(c10, 6)
    c7 = DistrictLeader(7, 'Citizen 7', 3007, 'Builder', 58, 'D7')
    s.add_citizen(c7, 4)
    return s


def society_from_file_demo() -> Society:
    """Return the Society defined in the provided file citizens.csv.
    """
    return create_society_from_file(open("citizens.csv"))


def promote_citizen_example() -> Society:
    """Return the society used in the handout example of promotion.
    """
    c = DistrictLeader(6, "Star", 3036, "CFO", 20, "Area 52")
    c2 = DistrictLeader(5, "S.T.A.R.R.Y Lab", 3024, "Manager", 50, "Finance")
    c3 = Citizen(7, "Hookins", 3071, "Labourer", 60)
    c4 = Citizen(11, "Starky", 3036, "Repairer", 90)
    c5 = Citizen(13, "STARRY", 3098, "Eng", 86)
    s = Society()
    s.add_citizen(c)
    s.add_citizen(c2, 6)
    s.add_citizen(c3, 5)
    s.add_citizen(c4, 7)
    s.add_citizen(c5, 7)
    return s


###########################################################################
# Tests for methods in Task 1.1
###########################################################################


def test_add_subordinate() -> None:
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c.add_subordinate(c1)
    assert c.get_direct_subordinates()[0] is c1
    assert c1.get_superior() is c


def test_add_subordinate_empty() -> None:
    c = Citizen(1, 'Citizen 1', 1000, 's', 10)
    c1 = Citizen(2, 'Citizen 2', 1000, 's', 20)
    c.add_subordinate(c1)
    assert c.get_direct_subordinates()[0] is c1
    assert c1.get_superior() is c


def test_add_subordinate_start() -> None:
    c = Citizen(1, 'Citizen 1', 1000, 's', 10)
    c1 = Citizen(2, 'Citizen 2', 1000, 's', 20)
    c2 = Citizen(3, 'Citizen 3', 1000, 's', 30)
    c.add_subordinate(c1)
    c.add_subordinate(c2)
    assert c.get_direct_subordinates()[0] is c1
    assert c.get_direct_subordinates()[1] is c2
    assert c1.get_superior() is c
    assert c2.get_superior() is c


def test_add_subordinate_middle() -> None:
    c = Citizen(0, 'Citizen 1', 1000, 's', 10)
    c1 = Citizen(1, 'Citizen 2', 1000, 's', 20)
    c2 = Citizen(2, 'Citizen 3', 1000, 's', 30)
    c3 = Citizen(3, 'Citizen 3', 1000, 's', 30)
    c4 = Citizen(4, 'Citizen 3', 1000, 's', 30)
    c5 = Citizen(5, 'Citizen 3', 1000, 's', 30)
    c.add_subordinate(c1)
    c.add_subordinate(c2)
    c.add_subordinate(c4)
    c.add_subordinate(c5)
    assert c.get_direct_subordinates() == [c1, c2, c4, c5]
    c.add_subordinate(c3)
    assert c.get_direct_subordinates() == [c1, c2, c3, c4, c5]


def test_add_subordinate_last() -> None:
    c = Citizen(0, 'Citizen 1', 1000, 's', 10)
    c1 = Citizen(1, 'Citizen 2', 1000, 's', 20)
    c2 = Citizen(2, 'Citizen 3', 1000, 's', 30)
    c3 = Citizen(3, 'Citizen 3', 1000, 's', 30)
    c4 = Citizen(4, 'Citizen 3', 1000, 's', 30)
    c5 = Citizen(5, 'Citizen 3', 1000, 's', 30)
    c.add_subordinate(c1)
    c.add_subordinate(c2)
    c.add_subordinate(c3)
    c.add_subordinate(c4)
    assert c.get_direct_subordinates() == [c1, c2, c3, c4]
    c.add_subordinate(c5)
    assert c.get_direct_subordinates() == [c1, c2, c3, c4, c5]


def test_remove_subordinate() -> None:
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c.add_subordinate(c1)
    c.remove_subordinate(11)
    assert c.get_direct_subordinates() == []
    assert c1.get_superior() is None


def test_remove_subordinate_2() -> None:
    c = Citizen(0, 'Citizen 0', 1000, 's', 10)
    c1 = Citizen(1, 'Citizen 1', 1000, 's', 20)
    c2 = Citizen(2, 'Citizen 2', 1000, 's', 30)
    c.add_subordinate(c1)
    c.add_subordinate(c2)
    assert c.get_direct_subordinates() == [c1, c2]
    c.remove_subordinate(1)
    assert c.get_direct_subordinates() == [c2]
    c.remove_subordinate(2)
    assert c.get_direct_subordinates() == []


def test_remove_subordinate_last() -> None:
    c = Citizen(0, 'Citizen 0', 1000, 's', 10)
    c1 = Citizen(1, 'Citizen 1', 1000, 's', 20)
    c2 = Citizen(2, 'Citizen 2', 1000, 's', 30)
    c3 = Citizen(3, 'Citizen 3', 1000, 's', 30)
    c.add_subordinate(c1)
    c.add_subordinate(c2)
    c.add_subordinate(c3)
    assert c.get_direct_subordinates() == [c1, c2, c3]
    c.remove_subordinate(3)
    assert c.get_direct_subordinates() == [c1, c2]
    c.remove_subordinate(2)
    assert c.get_direct_subordinates() == [c1]
    assert c2.get_superior() is None
    assert c3.get_superior() is None


def test_become_subordinate_to() -> None:
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c1.become_subordinate_to(c)
    assert c.get_direct_subordinates()[0] is c1
    assert c1.get_superior() is c


def test_become_subordinate_to_with_sub_to_same() -> None:
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c2 = Citizen(12, 'Citizen 12', 3011, 'Watcher', 25)
    c3 = Citizen(13, 'Citizen 13', 3011, 'Watcher', 25)
    c4 = Citizen(14, 'Citizen 14', 3011, 'Watcher', 25)
    c.add_subordinate(c1)
    c.add_subordinate(c2)
    c2.add_subordinate(c3)
    c2.add_subordinate(c4)
    assert c2.get_direct_subordinates() == [c3, c4]
    c2.become_subordinate_to(c1)
    assert c.get_direct_subordinates() == [c1]
    assert c1.get_direct_subordinates() == [c2]
    assert c1.get_all_subordinates() == [c2, c3, c4]


def test_become_subordinate_to_with_sub_to_lower() -> None:
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c2 = Citizen(12, 'Citizen 12', 3011, 'Watcher', 25)
    c3 = Citizen(13, 'Citizen 13', 3011, 'Watcher', 25)
    c4 = Citizen(14, 'Citizen 14', 3011, 'Watcher', 25)
    c.add_subordinate(c1)
    c.add_subordinate(c2)
    c1.add_subordinate(c3)
    c1.add_subordinate(c4)
    c2.become_subordinate_to(c1)
    assert c.get_direct_subordinates() == [c1]
    assert c1.get_direct_subordinates() == [c2, c3, c4]
    assert c2.get_superior() == c1
    assert c3.get_superior() == c1
    c3.become_subordinate_to(c)
    assert c1.get_direct_subordinates() == [c2, c4]
    assert c.get_direct_subordinates() == [c1, c3]


def test_become_subordinate_to_with_no_superior() -> None:
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    assert c1.get_superior() is None
    c1.become_subordinate_to(c)
    assert c.get_direct_subordinates() == [c1]
    assert c1.get_superior() == c


def test_get_citizen() -> None:
    c5 = Citizen(5, 'Citizen 5', 3005, 'Farmer', 101)
    who = c5.get_citizen(5)
    assert [who.cid, who.manufacturer, who.model_year, who.job, who.rating] == \
           [5, 'Citizen 5', 3005, 'Farmer', 101]


def test_get_citizen_right_on_the_citizen() -> None:
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    assert c.get_citizen(1) == c


def test_get_citizen_second_level() -> None:
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c.add_subordinate(c1)
    assert c.get_citizen(11) == c1


def test_get_citizen_third_level_multiple() -> None:
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c2 = Citizen(12, 'Citizen 12', 3011, 'Watcher', 25)
    c3 = Citizen(13, 'Citizen 13', 3011, 'Watcher', 25)
    c.add_subordinate(c1)
    c1.add_subordinate(c2)
    c1.add_subordinate(c3)
    assert c.get_citizen(13) == c3


def test_get_citizen_not_in() -> None:
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c2 = Citizen(12, 'Citizen 12', 3011, 'Watcher', 25)
    c3 = Citizen(13, 'Citizen 13', 3011, 'Watcher', 25)
    c4 = Citizen(14, 'Citizen 14', 3011, 'Watcher', 25)
    c.add_subordinate(c1)
    c.add_subordinate(c2)
    c1.add_subordinate(c3)
    c2.add_subordinate(c4)
    assert c.get_citizen(11) == c1
    assert c.get_citizen(12) == c2
    assert c.get_citizen(13) == c3
    assert c.get_citizen(14) == c4
    assert c.get_citizen(15) is None


def test_get_citizen_two_long_term() -> None:
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c2 = Citizen(12, 'Citizen 12', 3011, 'Watcher', 25)
    c3 = Citizen(13, 'Citizen 13', 3011, 'Watcher', 25)
    c4 = Citizen(14, 'Citizen 14', 3011, 'Watcher', 25)
    c5 = Citizen(15, 'Citizen 14', 3011, 'Watcher', 25)
    c6 = Citizen(16, 'Citizen 14', 3011, 'Watcher', 25)
    c7 = Citizen(17, 'Citizen 14', 3011, 'Watcher', 25)
    c8 = Citizen(18, 'Citizen 14', 3011, 'Watcher', 25)
    c.add_subordinate(c1)
    c.add_subordinate(c2)
    c1.add_subordinate(c3)
    c3.add_subordinate(c4)
    c4.add_subordinate(c5)
    c2.add_subordinate(c6)
    c6.add_subordinate(c7)
    c7.add_subordinate(c8)
    assert c.get_citizen(18) == c8
    assert c.get_citizen(15) == c5
    assert c.get_citizen(99) is None


###########################################################################
# Tests for methods in Task 1.2
###########################################################################

def test_get_all_subordinates() -> None:
    c1 = Citizen(10, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c1.become_subordinate_to(c2)
    c2.become_subordinate_to(c3)
    result = c3.get_all_subordinates()
    assert result == [c2, c1]


def test_all_subordinates_empty() -> None:
    c = Citizen(0, "Starky Industries", 3024, "Labourer", 50)
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Starky Industries", 3024, "Labourer", 50)
    c3 = Citizen(3, "Starky Industries", 3024, "Labourer", 50)
    c4 = Citizen(4, "Starky Industries", 3024, "Labourer", 50)
    assert c.get_all_subordinates() == []


def test_all_subordinates_many() -> None:
    c = Citizen(0, "Starky Industries", 3024, "Labourer", 50)
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Starky Industries", 3024, "Labourer", 50)
    c3 = Citizen(3, "Starky Industries", 3024, "Labourer", 50)
    c4 = Citizen(4, "Starky Industries", 3024, "Labourer", 50)
    c.add_subordinate(c1)
    c.add_subordinate(c2)
    c.add_subordinate(c3)
    c.add_subordinate(c4)
    assert c.get_all_subordinates() == [c1, c2, c3, c4]


def test_all_subordinates_three_level() -> None:
    c = Citizen(0, "Starky Industries", 3024, "Labourer", 50)
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Starky Industries", 3024, "Labourer", 50)
    c3 = Citizen(3, "Starky Industries", 3024, "Labourer", 50)
    c4 = Citizen(4, "Starky Industries", 3024, "Labourer", 50)
    c5 = Citizen(5, "Starky Industries", 3024, "Labourer", 50)
    c6 = Citizen(6, "Starky Industries", 3024, "Labourer", 50)
    c7 = Citizen(7, "Starky Industries", 3024, "Labourer", 50)
    c8 = Citizen(8, "Starky Industries", 3024, "Labourer", 50)
    c.add_subordinate(c1)
    c.add_subordinate(c2)
    c2.add_subordinate(c3)
    c2.add_subordinate(c4)
    c3.add_subordinate(c5)
    c1.add_subordinate(c6)
    c6.add_subordinate(c7)
    c7.add_subordinate(c8)
    assert c.get_all_subordinates() == [c1, c2, c3, c4, c5, c6, c7, c8]


def test_get_society_head() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c1.become_subordinate_to(c2)
    c2.become_subordinate_to(c3)
    head = c1.get_society_head()
    assert head is c3


def test_get_society_head_self() -> None:
    c = Citizen(0, "Starky Industries", 3024, "Labourer", 50)
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    assert c.get_society_head() == c
    c1.become_subordinate_to(c)
    c2.become_subordinate_to(c)
    c3.become_subordinate_to(c)
    assert c1.get_society_head() == c
    assert c2.get_society_head() == c
    assert c3.get_society_head() == c
    c4 = Citizen(4, "Starky Industries", 3024, "Labourer", 50)
    c5 = Citizen(5, "Hookins National Lab", 3024, "Manager", 30)
    c6 = Citizen(6, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c4.become_subordinate_to(c1)
    c5.become_subordinate_to(c2)
    c6.become_subordinate_to(c3)
    assert c4.get_society_head() == c
    assert c5.get_society_head() == c
    assert c6.get_society_head() == c


def test_get_closest_common_superior() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c4 = Citizen(4, "Starky Industries", 3022, "Manager", 55)
    c5 = Citizen(5, "Hookins National Lab", 3023, "Engineer", 50)
    c1.become_subordinate_to(c2)
    c2.become_subordinate_to(c3)
    c4.become_subordinate_to(c3)
    c5.become_subordinate_to(c4)
    assert c3.get_closest_common_superior(1) == c3


def test_get_closest_common_superior_self() -> None:
    c = Citizen(0, "Starky Industries", 3024, "Labourer", 50)
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    assert c.get_closest_common_superior(0) == c


def test_get_closest_common_superior_same_level() -> None:
    c = Citizen(0, "Starky Industries", 3024, "Labourer", 50)
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c1.become_subordinate_to(c)
    c2.become_subordinate_to(c)
    c3.become_subordinate_to(c)
    assert c1.get_superior() == c
    assert c2.get_superior() == c
    assert c3.get_superior() == c
    assert c1.get_closest_common_superior(2) == c
    assert c2.get_closest_common_superior(1) == c
    assert c3.get_closest_common_superior(2) == c
    assert c3.get_closest_common_superior(3) == c3
    assert c2.get_closest_common_superior(2) == c2
    assert c1.get_closest_common_superior(1) == c1


def test_get_closest_common_superior_two_branch() -> None:
    c = Citizen(0, "Starky Industries", 3024, "Labourer", 50)
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c11 = Citizen(11, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c12 = Citizen(12, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c13 = Citizen(13, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c21 = Citizen(21, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c22 = Citizen(22, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c23 = Citizen(23, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c1.become_subordinate_to(c)
    c2.become_subordinate_to(c)
    c11.become_subordinate_to(c1)
    c12.become_subordinate_to(c11)
    c13.become_subordinate_to(c12)
    c21.become_subordinate_to(c2)
    c22.become_subordinate_to(c21)
    c23.become_subordinate_to(c22)
    assert c13.get_closest_common_superior(23) == c
    assert c12.get_closest_common_superior(22) == c
    assert c11.get_closest_common_superior(21) == c
    assert c13.get_closest_common_superior(12) == c12
    assert c12.get_closest_common_superior(11) == c11
    assert c23.get_closest_common_superior(22) == c22
    assert c22.get_closest_common_superior(21) == c21
    assert c23.get_closest_common_superior(0) == c


###########################################################################
# Tests for methods in Task 1.3
###########################################################################


def test_society_get_citizen() -> None:
    s = sample_society0()
    who = s.get_citizen(5)
    assert [who.cid, who.manufacturer, who.model_year, who.job, who.rating] == \
           [5, 'Citizen 5', 3005, 'Farmer', 101]


def test_society_have_none() -> None:
    c = Citizen(0, "Starky Industries", 3024, "Labourer", 50)
    s = Society(c)
    assert s.get_citizen(1) is None


def test_society_without_head() -> None:
    s = Society()
    assert s.get_citizen(1) is None
    assert s.get_citizen(99) is None


def test_society_get_citizen_first_level() -> None:
    c = Citizen(0, "Starky Industries", 3024, "Labourer", 50)
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c.add_subordinate(c1)
    c.add_subordinate(c2)
    s = Society(c)
    assert s.get_citizen(1) == c1
    assert s.get_citizen(2) == c2


def test_society_get_citizen_two_level() -> None:
    c = Citizen(0, "Starky Industries", 3024, "Labourer", 50)
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c.add_subordinate(c1)
    c1.add_subordinate(c2)
    s = Society(c)
    assert s.get_citizen(1) == c1
    assert s.get_citizen(2) == c2


def test_get_all_citizens() -> None:
    s = sample_society0()
    result = [c.cid for c in s.get_all_citizens()]
    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_add_citizen() -> None:
    s = Society()
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Some Lab", 3024, "Lawyer", 30)
    s.add_citizen(c2)
    s.add_citizen(c1, 2)
    assert s.get_head() == c2
    assert s.get_citizen(1) is c1
    assert c1.get_superior() is c2


def test_get_citizens_with_job() -> None:
    s = sample_society0()
    result = [c.cid for c in s.get_citizens_with_job('Farmer')]
    assert result == [5, 8, 9]


###########################################################################
# Tests for methods in Task 2.1
###########################################################################

def test_district_leader() -> None:
    d = DistrictLeader(2, "Some Lab", 3024, "Lawyer", 30, "District A")
    assert [d.cid, d.manufacturer, d.model_year, d.job, d.rating] == \
           [2, "Some Lab", 3024, "Lawyer", 30]
    assert d.get_district_name() == 'District A'


def test_get_district_citizens() -> None:
    c1 = DistrictLeader(1, "Some Lab", 3024, "Commander", 65, "District A")
    c2 = Citizen(2, "Hookins National Lab", 3024, "Lawyer", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Labourer", 55)
    c2.become_subordinate_to(c1)
    c3.become_subordinate_to(c1)
    assert c1.get_district_citizens() == [c1, c2, c3]


###########################################################################
# Tests for methods in Task 2.2
###########################################################################


def test_get_district_name() -> None:
    s = sample_society1()
    who = s.get_citizen(10)
    result = who.get_district_name()
    assert result == 'D2'


def test_rename_district() -> None:
    s = sample_society1()
    who = s.get_citizen(10)
    who.rename_district('D10')
    leader = s.get_citizen(2)
    assert leader.get_district_name() == 'D10'


###########################################################################
# Tests for method in Task 2.3
###########################################################################

def test_change_citizen_type() -> None:
    s = sample_society1()
    s.change_citizen_type(6, 'D6')
    who = s.get_citizen(6)
    assert isinstance(who, DistrictLeader)
    assert who.get_district_name() == 'D6'
    assert [c.cid for c in who.get_all_subordinates()] == [8, 9, 10]
    assert who.get_superior().cid == 2


def test_change_citizen_type_single() -> None:
    c = Citizen(0, "Starky Industries", 3024, "Labourer", 50)
    c1 = DistrictLeader(1, "Starky Industries", 3024, "Labourer", 50, 'a')
    s = Society(c)
    s2 = Society(c1)
    s.change_citizen_type(0, 'a')
    s2.change_citizen_type(1)

    assert isinstance(s.get_head(), DistrictLeader)
    assert isinstance(s2.get_head(), Citizen)


def test_change_citizen_type_middle() -> None:
    c = Citizen(0, "Starky Industries", 3024, "Labourer", 50)
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Starky Industries", 3024, "Labourer", 50)
    c3 = Citizen(3, "Starky Industries", 3024, "Labourer", 50)
    c4 = DistrictLeader(4, "Starky Industries", 3024, "Labourer", 50, 'b')
    c5 = Citizen(5, "Starky Industries", 3024, "Labourer", 50)
    c6 = Citizen(6, "Starky Industries", 3024, "Labourer", 50)
    c.add_subordinate(c1)
    c1.add_subordinate(c2)
    c2.add_subordinate(c3)
    c.add_subordinate(c4)
    c4.add_subordinate(c5)
    c5.add_subordinate(c6)
    assert c.get_direct_subordinates() == [c1, c4]
    s = Society(c)
    t1 = s.change_citizen_type(1, 'a')
    t2 = s.change_citizen_type(4)
    assert isinstance(s.get_citizen(1), DistrictLeader)
    assert isinstance(s.get_citizen(4), Citizen)
    assert c.get_direct_subordinates() == [t1, t2]
    assert s.get_citizen(1).get_superior() == c
    assert s.get_citizen(4).get_superior() == c
    assert s.get_citizen(1).get_direct_subordinates() == [c2]
    assert s.get_citizen(4).get_direct_subordinates() == [c5]


def test_change_citizen_type_last() -> None:
    c = Citizen(0, "Starky Industries", 3024, "Labourer", 50)
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Starky Industries", 3024, "Labourer", 50)
    c3 = Citizen(3, "Starky Industries", 3024, "Labourer", 50)
    c4 = Citizen(4, "Starky Industries", 3024, "Labourer", 50)
    c5 = Citizen(5, "Starky Industries", 3024, "Labourer", 50)
    c6 = DistrictLeader(6, "Starky Industries", 3024, "Labourer", 50, 'b')
    c.add_subordinate(c1)
    c1.add_subordinate(c2)
    c2.add_subordinate(c3)
    c.add_subordinate(c4)
    c4.add_subordinate(c5)
    c5.add_subordinate(c6)
    s = Society(c)
    t1 = s.change_citizen_type(3, 'a')
    t2 = s.change_citizen_type(6)
    assert c2.get_direct_subordinates() == [t1]
    assert c5.get_direct_subordinates() == [t2]
    assert isinstance(c2.get_direct_subordinates()[0], DistrictLeader)
    assert isinstance(c5.get_direct_subordinates()[0], Citizen)
    assert c.get_all_subordinates() == [c1, c2, t1, c4, c5, t2]


###########################################################################
# Tests for method in Task 3.1
###########################################################################

def test_swap_up_second_level() -> None:
    c1 = Citizen(1, 'Name 1', 500, "HHH", 30)
    c2 = Citizen(2, 'Name 2', 1000, "AAA", 50)
    c1.add_subordinate(c2)
    s = Society(c1)
    s_new = s._swap_up(c2)
    assert s_new.cid == 2
    assert s_new.manufacturer == 'Name 2'
    assert s_new.model_year == 1000
    assert s_new.job == "HHH"
    assert s_new.rating == 50
    assert s._head == c2
    assert c2 == s_new
    assert c2.job == "HHH"
    assert c1.job == "AAA"
    assert c2.get_direct_subordinates()[0] == c1
    assert s.get_all_citizens() == [c1, c2]
    assert c2.get_superior() is None
    assert c1.get_superior() == c2


def test_swap_up_secondlevel_with_sub() -> None:
    c1 = Citizen(1, 'Name 1', 500, "AAA", 30)
    c2 = Citizen(2, 'Name 2', 1000, "BBB", 50)
    c3 = Citizen(3, 'Name 3', 1000, "CCC", 50)
    c4 = Citizen(4, 'Name 4', 1000, "DDD", 50)
    c5 = Citizen(5, 'Name 4', 1000, "EEE", 50)
    c6 = Citizen(6, 'Name 4', 1000, "FFF", 50)
    c7 = Citizen(7, 'Name 4', 1000, "GGG", 50)
    c1.add_subordinate(c2)
    c1.add_subordinate(c3)
    c2.add_subordinate(c4)
    c2.add_subordinate(c5)
    c3.add_subordinate(c6)
    c3.add_subordinate(c7)
    s = Society(c1)

    s._swap_up(c2)
    assert s._head == c2
    assert s._head.job == "AAA"
    assert c1.job == "BBB"
    assert c2.job == "AAA"
    assert s._head.get_direct_subordinates()[0].job == "BBB"
    assert c1.get_direct_subordinates() == [c4, c5]
    assert c2.get_direct_subordinates() == [c1, c3]
    assert c3.get_superior() == c2

    s._swap_up(c3)
    assert s._head == c3
    assert c3.job == "AAA"
    assert c1.job == "BBB"
    assert c2.job == "CCC"
    assert c3.get_direct_subordinates() == [c1, c2]
    assert c1.get_direct_subordinates() == [c4, c5]
    assert c2.get_direct_subordinates() == [c6, c7]
    assert c2.get_superior() == c3
    assert c1.get_superior() == c3


def test_swap_up_downest_level() -> None:
    c1 = Citizen(1, 'Name 1', 500, "AAA", 30)
    c2 = Citizen(2, 'Name 2', 1000, "BBB", 50)
    c3 = Citizen(3, 'Name 3', 1000, "CCC", 50)
    c4 = Citizen(4, 'Name 4', 1000, "DDD", 50)
    c5 = Citizen(5, 'Name 4', 1000, "EEE", 50)
    c6 = Citizen(6, 'Name 4', 1000, "FFF", 50)
    c7 = Citizen(7, 'Name 4', 1000, "GGG", 50)
    c1.add_subordinate(c2)
    c1.add_subordinate(c3)
    c2.add_subordinate(c4)
    c2.add_subordinate(c5)
    c3.add_subordinate(c6)
    c3.add_subordinate(c7)
    s = Society(c1)
    s._swap_up(c4)
    s._swap_up(c6)

    assert c4.get_direct_subordinates() == [c2, c5]
    assert c6.get_direct_subordinates() == [c3, c7]
    assert c2.get_direct_subordinates() == []
    assert c3.get_direct_subordinates() == []
    assert c1.get_direct_subordinates() == [c4, c6]
    assert c4.get_superior() == c1
    assert c6.get_superior() == c1
    assert c1.get_superior() is None
    assert s.get_head() == c1


def test_promote_citizen() -> None:
    s = promote_citizen_example()
    s.promote_citizen(11)
    promoted = s.get_citizen(11)
    demoted = s.get_citizen(5)
    assert isinstance(promoted, DistrictLeader)
    assert promoted.get_district_name() == 'Finance'
    assert [c.cid for c in promoted.get_all_subordinates()] == [5, 7, 13]
    assert promoted.get_superior().cid == 6
    assert not isinstance(demoted, DistrictLeader)
    assert [c.cid for c in demoted.get_all_subordinates()] == [7, 13]
    assert demoted.get_superior() == promoted


def test_promote_citizen_until_districtleader() -> None:
    c1 = Citizen(1, 'Name 1', 500, "AAA", 30)
    c2 = DistrictLeader(2, 'Name 2', 1000, "BBB", 50, 'a')
    c3 = Citizen(3, 'Name 3', 1000, "CCC", 50)
    c4 = Citizen(4, 'Name 4', 1000, "DDD", 50)
    c5 = Citizen(5, 'Name 4', 1000, "EEE", 50)
    c6 = Citizen(6, 'Name 4', 1000, "FFF", 50)
    c7 = Citizen(7, 'Name 4', 1000, "GGG", 50)
    c2.become_subordinate_to(c1)
    c3.become_subordinate_to(c2)
    c4.become_subordinate_to(c3)
    c5.become_subordinate_to(c4)
    c6.become_subordinate_to(c5)
    c7.become_subordinate_to(c6)
    s = Society(c1)
    s.promote_citizen(7)
    new_second_one = c1.get_direct_subordinates()[0]
    assert new_second_one.cid == 7
    assert new_second_one.job == "BBB"
    after_one = new_second_one.get_direct_subordinates()[0]
    assert after_one.cid == 2
    assert after_one.get_direct_subordinates()[0].cid == 3

def test_promote_not_movable() -> None:
    c1 = Citizen(1, 'Name 1', 1000, "AAA", 30)
    c2 = Citizen(2, 'Name 2', 1000, "BBB", 50)
    c3 = Citizen(3, 'Name 3', 1000, "CCC", 50)
    c4 = Citizen(4, 'Name 4', 1000, "DDD", 50)
    c5 = Citizen(5, 'Name 4', 1000, "EEE", 50)
    c6 = Citizen(6, 'Name 4', 1000, "FFF", 100)
    c7 = Citizen(7, 'Name 4', 1000, "GGG", 50)
    c2.become_subordinate_to(c1)
    c3.become_subordinate_to(c2)
    c4.become_subordinate_to(c3)
    c5.become_subordinate_to(c4)
    c6.become_subordinate_to(c5)
    c7.become_subordinate_to(c6)
    s = Society(c1)
    s.promote_citizen(7)
    assert c6.get_direct_subordinates()[0] == c7
    assert c7.get_direct_subordinates() == []

def test_promote_citizen_head() -> None:
    c1 = Citizen(1, 'Name 1', 1000, "AAA", 30)
    c2 = Citizen(2, 'Name 2', 1000, "BBB", 50)
    c3 = Citizen(3, 'Name 3', 1000, "CCC", 50)
    c4 = Citizen(4, 'Name 4', 1000, "DDD", 50)
    c5 = Citizen(5, 'Name 5', 1000, "EEE", 50)
    c6 = Citizen(6, 'Name 6', 1000, "FFF", 50)
    c7 = Citizen(7, 'Name 7', 1000, "GGG", 50)
    c1.add_subordinate(c2)
    c2.add_subordinate(c3)
    c3.add_subordinate(c4)
    c4.add_subordinate(c5)
    c5.add_subordinate(c6)
    c6.add_subordinate(c7)
    s = Society(c1)
    s.promote_citizen(7)
    assert s.get_head().cid == 7

def test_promote_small_branch() -> None:
    c1 = Citizen(1, 'Name 1', 1000, "AAA", 60)
    c2 = Citizen(2, 'Name 2', 1000, "BBB", 60)
    c3 = Citizen(3, 'Name 3', 1000, "CCC", 60)
    c4 = Citizen(4, 'Name 4', 1000, "DDD", 60)
    c5 = Citizen(5, 'Name 5', 1000, "EEE", 50)
    c6 = Citizen(6, 'Name 6', 1000, "FFF", 50)
    c7 = Citizen(7, 'Name 7', 1000, "GGG", 50)
    c1.add_subordinate(c2)
    c2.add_subordinate(c3)
    c3.add_subordinate(c4)
    c4.add_subordinate(c5)
    c5.add_subordinate(c6)
    c5.add_subordinate(c7)
    s = Society(c1)
    s.promote_citizen(6)
    assert c4.get_direct_subordinates() == [c6]

def test_promote_citizen_test_district_certain() -> None:
    c1 = Citizen(1, 'Name 1', 1000, "AAA", 60)
    c2 = DistrictLeader(2, 'Name 2', 1000, "BBB", 60,'a')
    c3 = DistrictLeader(3, 'Name 3', 1000, "CCC", 60,'b')
    c4 = Citizen(4, 'Name 4', 1000, "DDD", 60)
    c5 = Citizen(5, 'Name 5', 1000, "EEE", 60)
    c6 = Citizen(6, 'Name 6', 1000, "FFF", 60)
    c7 = Citizen(7, 'Name 7', 1000, "GGG", 60)
    c1.add_subordinate(c2)
    c1.add_subordinate(c3)
    c2.add_subordinate(c4)
    c2.add_subordinate(c5)
    c3.add_subordinate(c6)
    c3.add_subordinate(c7)
    s = Society(c1)
    s.promote_citizen(5)
    s.promote_citizen(7)
    assert c1.get_direct_subordinates()[0].cid == 5
    assert c1.get_direct_subordinates()[1].cid == 7
    assert c1.get_direct_subordinates()[0].get_district_name() == 'a'
    assert c1.get_direct_subordinates()[1].get_district_name() == 'b'
    t1 = c1.get_direct_subordinates()[0]
    assert t1.get_direct_subordinates()[0].cid == 2
    assert t1.get_direct_subordinates()[1].cid == 4
    assert isinstance(t1.get_direct_subordinates()[0], Citizen)
    assert isinstance(t1.get_direct_subordinates()[1], Citizen)

    t2 = c1.get_direct_subordinates()[1]
    assert t2.get_direct_subordinates()[0].cid == 3
    assert t2.get_direct_subordinates()[1].cid == 6
    assert isinstance(t2.get_direct_subordinates()[0], Citizen)
    assert isinstance(t2.get_direct_subordinates()[1], Citizen)






###########################################################################
# Tests for method in Task 3.2
###########################################################################

def test_get_highest_rated_subordinate() -> None:
    s = sample_society1()
    who = s.get_citizen(2)
    result = who.get_highest_rated_subordinate()
    assert result.cid == 5


def test_delete_citizen() -> None:
    s = sample_society1()
    s.delete_citizen(6)
    who = s.get_citizen(2)
    assert [c.cid for c in who.get_direct_subordinates()] == [5, 8, 9, 10]
    assert s.get_citizen(6) is None


if __name__ == '__main__':
    import pytest

    pytest.main(['a2_sample_test_b.py'])

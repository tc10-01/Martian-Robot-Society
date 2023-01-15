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
from hypothesis import given
from hypothesis.strategies import integers


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

def sample_society2() -> Society:
    """Return a Society of sufficient complexity with District leaders.
    Only 1 Citizen, not district leader
    """
    s = Society()
    c1 = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    s.add_citizen(c1)
    return s

def sample_society3() -> Society:
    """Return a Society of sufficient complexity with District leaders.
    Only 1 Citizen, is district leader
    """
    s = Society()
    c1 = DistrictLeader(1, 'Citizen 1', 3001, 'Big boss', 10, 'D1')
    s.add_citizen(c1)
    return s

def sample_society4() -> Society:
    """Return a Society of sufficient complexity with District leaders.
    1 head, 1 subordinate, both citizens
    """
    s = Society()
    c1 = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    s.add_citizen(c1)
    c2 = Citizen(2, 'Citizen 2', 3002, 'Bank robber', 19,)
    s.add_citizen(c2, 1)
    return s


def sample_society5() -> Society:
    """Return a Society of sufficient complexity with District leaders.
    1 head, 1 subordinate, both district leaders
    """
    s = Society()
    c1 = DistrictLeader(1, 'Citizen 1', 3001, 'Big boss', 10, 'D1')
    s.add_citizen(c1)
    c2 = DistrictLeader(2, 'Citizen 2', 3002, 'Bank robber', 19, 'D2')
    s.add_citizen(c2, 1)
    return s


def sample_society6() -> Society:
    """Return a Society of sufficient complexity with District leaders.
    1 head, 1 subordinate, head is citizen, subordinate is district
    """
    s = Society()
    c1 = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10,)
    s.add_citizen(c1)
    c2 = DistrictLeader(2, 'Citizen 2', 3002, 'Bank robber', 19, 'D2')
    s.add_citizen(c2, 1)
    return s


def sample_society7() -> Society:
    """Return a Society of sufficient complexity with District leaders.
    1 head, 1 subordinate, head is district leader, subordinate is citizen
    """
    s = Society()
    c1 = DistrictLeader(1, 'Citizen 1', 3001, 'Big boss', 10, 'D1')
    s.add_citizen(c1)
    c2 = Citizen(2, 'Citizen 2', 3002, 'Bank robber', 19)
    s.add_citizen(c2, 1)
    return s

def sample_society8() -> Society:
    """Return a Society of sufficient complexity with District leaders.
    Change is making c4 higher rated than c3
    """
    s = Society()
    c1 = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    s.add_citizen(c1)
    c2 = DistrictLeader(2, 'Citizen 2', 3002, 'Bank robber', 19, 'D2')
    c3 = Citizen(3, 'Citizen 3', 3003, 'Cook', 5)
    c4 = Citizen(4, 'Citizen 4', 3004, 'Cook', 82)
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

def sample_society9() -> Society:
    """Return an empty society
    """
    s = Society(None)
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


def test_add_subordinate_non_head() -> None:
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c2 = Citizen(2, 'Citizen 11', 3011, 'Watcher', 25)
    c3 = Citizen(3, 'Citizen 11', 3011, 'Watcher', 25)
    c.add_subordinate(c1)
    c1.add_subordinate(c3)
    c1.add_subordinate(c2)
    assert c.get_direct_subordinates()[0] is c1
    assert c1.get_superior() is c
    assert c1.get_direct_subordinates()[0] is c2
    assert c1.get_direct_subordinates()[1] is c3
    assert c2.get_superior() is c1
    assert c3.get_superior() is c1


def test_add_subordinate_v2() -> None:
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c1.add_subordinate(c)
    assert c1.get_direct_subordinates()[0] is c
    assert c.get_superior() is c1


def test_add_subordinate_v3() -> None:
    c = DistrictLeader(1, 'Citizen 1', 3001, 'Big boss', 10, "District A")
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c1.add_subordinate(c)
    assert c1.get_direct_subordinates()[0] is c
    assert c.get_superior() is c1


def test_add_subordinate_v4() -> None:
    c = DistrictLeader(1, 'Citizen 1', 3001, 'Big boss', 10, "District A")
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c.add_subordinate(c1)
    assert c.get_direct_subordinates()[0] is c1
    assert c1.get_superior() is c


def test_remove_subordinate() -> None:
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c.add_subordinate(c1)
    c.remove_subordinate(11)
    assert c.get_direct_subordinates() == []
    assert c1.get_superior() is None


def test_remove_subordinate_multiple_sub_for_head() -> None:
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c2 = Citizen(2, 'Citizen 11', 3011, 'Watcher', 25)
    c.add_subordinate(c1)
    c.add_subordinate(c2)
    c.remove_subordinate(11)
    assert c.get_direct_subordinates()[0].cid == 2
    assert c1.get_superior() is None
    assert c2.get_superior() is c


def test_remove_subordinate_single_sub_non_head() -> None:
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c2 = Citizen(2, 'Citizen 11', 3011, 'Watcher', 25)
    c.add_subordinate(c1)
    c1.add_subordinate(c2)
    c1.remove_subordinate(2)
    assert c1.get_direct_subordinates() == []
    assert c2.get_superior() is None
    assert c1.get_superior() is c


def test_remove_subordinate_multiple_sub_non_head() -> None:
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c2 = Citizen(2, 'Citizen 11', 3011, 'Watcher', 25)
    c3 = Citizen(3, 'Citizen 11', 3011, 'Watcher', 25)
    c.add_subordinate(c1)
    c1.add_subordinate(c2)
    c1.add_subordinate(c3)
    c1.remove_subordinate(2)
    assert c1.get_direct_subordinates()[0].cid == 3
    assert c2.get_superior() is None
    assert c1.get_superior() is c


def test_add_subordinate_not_empty() -> None:
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c5 = Citizen(5, 'Citizen 5', 3005, 'Farmer', 101)
    c._subordinates = [c1]
    c.add_subordinate(c5)
    assert c.get_direct_subordinates()[0] is c5
    assert c.get_direct_subordinates()[1] is c1
    assert c5.get_superior() is c


def test_add_subordinate_not_empty_1() -> None:
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c5 = Citizen(5, 'Citizen 5', 3005, 'Farmer', 101)
    c._subordinates = [c5]
    c.add_subordinate(c1)
    assert c.get_direct_subordinates()[0] is c5
    assert c.get_direct_subordinates()[1] is c1
    assert c1.get_superior() is c


def test_add_subordinate_not_empty_2() -> None:
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c5 = Citizen(5, 'Citizen 5', 3005, 'Farmer', 101)
    c2 = Citizen(2, 'Citizen 2', 3005, 'Farmer', 101)
    c3 = Citizen(3, 'Citizen 3', 3005, 'Farmer', 101)
    c4 = Citizen(4, 'Citizen 4', 3005, 'Farmer', 101)
    c6 = Citizen(6, 'Citizen 4', 3005, 'Farmer', 101)
    c7 = Citizen(7, 'Citizen 4', 3005, 'Farmer', 101)
    c._subordinates = [c1, c2, c4, c5]
    c.add_subordinate(c3)
    c2.add_subordinate(c7)
    assert c.get_direct_subordinates()[2] is c3
    assert [x.cid for x in c.get_direct_subordinates()] == [11, 2, 3, 4, 5]
    assert [x.cid for x in c2.get_direct_subordinates()] == [7]
    c2.add_subordinate(c6)
    assert [x.cid for x in c2.get_direct_subordinates()] == [6, 7]
    assert c3.get_superior() is c
    assert c6.get_superior() is c2
    assert c7.get_superior() is c2


def test_remove_subordinate_one() -> None:
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c.add_subordinate(c1)
    c.remove_subordinate(11)
    assert c.get_direct_subordinates() == []
    assert c1.get_superior() is None


def test_remove_subordinate_1() -> None:
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c5 = Citizen(5, 'Citizen 5', 3005, 'Farmer', 101)
    c2 = Citizen(2, 'Citizen 2', 3005, 'Farmer', 101)
    c.add_subordinate(c1)
    c.add_subordinate(c2)
    c.add_subordinate(c5)
    c.remove_subordinate(11)
    assert c.get_direct_subordinates()[0] == c2
    assert c.get_direct_subordinates()[1] == c5
    assert c1.get_superior() is None


def test_remove_subordinate_2() -> None:
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c5 = Citizen(5, 'Citizen 5', 3005, 'Farmer', 101)
    c2 = Citizen(2, 'Citizen 2', 3005, 'Farmer', 101)
    c.add_subordinate(c1)
    c.add_subordinate(c2)
    c.add_subordinate(c5)
    c.remove_subordinate(5)
    assert c.get_direct_subordinates()[0] == c2
    assert c.get_direct_subordinates()[1] == c1
    assert c5.get_superior() is None


def test_remove_subordinate_two() -> None:
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c5 = Citizen(5, 'Citizen 5', 3005, 'Farmer', 101)
    c2 = Citizen(2, 'Citizen 2', 3005, 'Farmer', 101)
    c3 = Citizen(3, 'Citizen 2', 3005, 'Farmer', 101)
    c4 = Citizen(4, 'Citizen 2', 3005, 'Farmer', 101)
    c.add_subordinate(c1)
    c.add_subordinate(c2)
    c.add_subordinate(c5)
    c2.add_subordinate(c3)
    c2.add_subordinate(c4)
    c.remove_subordinate(2)
    assert c.get_direct_subordinates()[0] == c5
    assert c.get_direct_subordinates()[1] == c1
    assert c2.get_superior() is None


def test_become_subordinate_to_new() -> None:
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c1.become_subordinate_to(None)
    assert c1.get_superior() is None


def test_become_subordinate_to() -> None:
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c1.become_subordinate_to(c)
    assert c.get_direct_subordinates()[0] is c1
    assert c1.get_superior() is c


def test_become_subordinate_to_1() -> None:
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    assert c.get_superior() is None
    assert c1.get_superior() is None
    c1.become_subordinate_to(c)
    assert c.get_direct_subordinates()[0] is c1
    assert c1.get_superior() is c


def test_become_subordinate_to_superior_none_citizen_sup_none() -> None:
    c = None
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    assert c1.get_superior() is None
    c1.become_subordinate_to(c)
    assert c1.get_superior() is None


def test_become_subordinate_to_c2_subordinate_to_c3() -> None:
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c2 = Citizen(2, 'Citizen 11', 3011, 'Watcher', 25)
    c3 = Citizen(3, 'Citizen 11', 3011, 'Watcher', 25)
    c1.add_subordinate(c2)
    assert c2.get_superior().cid == 11
    c2.become_subordinate_to(c3)
    assert c2.get_superior().cid == 3
    assert c3.get_direct_subordinates()[0].cid == 2
    assert c1.get_direct_subordinates() == []


def test_become_subordinate_to_c1_sub_c2() -> None:
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c2 = Citizen(2, 'Citizen 11', 3011, 'Watcher', 25)
    c1.add_subordinate(c2)
    assert c2.get_superior().cid == 11
    assert c1.get_superior() is None
    c1.become_subordinate_to(c2)
    assert c2.get_superior() is None
    assert c1.get_superior() == c2
    assert c1.get_direct_subordinates() == []
    assert c2.get_direct_subordinates()[0] == 11


def test_become_subordinate_to_c1_sub_c3() -> None:
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c2 = Citizen(2, 'Citizen 11', 3011, 'Watcher', 25)
    c3 = Citizen(3, 'Citizen 11', 3011, 'Watcher', 25)
    c1.add_subordinate(c2)
    assert c2.get_superior().cid == 11
    assert c1.get_superior() is None
    c1.become_subordinate_to(c3)
    assert c1.get_superior() is c3
    assert c2.get_superior() is c1
    assert c3.get_superior() is None
    assert c1.get_direct_subordinates() == [c2]
    assert c2.get_direct_subordinates() == []
    assert c3.get_direct_subordinates() == [c1]


def test_become_subordinate_to_c2_sub_c1() -> None:
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c2 = Citizen(2, 'Citizen 11', 3011, 'Watcher', 25)
    c1.add_subordinate(c2)
    assert c2.get_superior().cid == 11
    assert c1.get_superior() is None
    c2.become_subordinate_to(c1)
    assert c1.get_superior() is None
    assert c2.get_superior() == c1
    assert c1.get_direct_subordinates() == [c2]
    assert c2.get_direct_subordinates() == []


def test_become_subordinate_to_c3_sub_c1() -> None:
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c2 = Citizen(2, 'Citizen 11', 3011, 'Watcher', 25)
    c3 = Citizen(3, 'Citizen 11', 3011, 'Watcher', 25)
    c1.add_subordinate(c2)
    assert c2.get_superior().cid == 11
    assert c1.get_superior() is None
    c3.become_subordinate_to(c1)
    assert c1.get_superior() is None
    assert c2.get_superior() is c1
    assert c3.get_superior() is c1
    assert c1.get_direct_subordinates() == [c2, c3]
    assert c2.get_direct_subordinates() == []
    assert c3.get_direct_subordinates() == []


def test_become_subordinate_to_c3_sub_c2() -> None:
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c2 = Citizen(2, 'Citizen 11', 3011, 'Watcher', 25)
    c3 = Citizen(3, 'Citizen 11', 3011, 'Watcher', 25)
    c1.add_subordinate(c2)
    assert c2.get_superior().cid == 11
    assert c1.get_superior() is None
    c3.become_subordinate_to(c2)
    assert c1.get_superior() is None
    assert c2.get_superior() is c1
    assert c3.get_superior() is c2
    assert c1.get_direct_subordinates() == [c2]
    assert c2.get_direct_subordinates() == [c3]
    assert c3.get_direct_subordinates() == []


def test_become_subordinate_to_v2() -> None:
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c1.become_subordinate_to(c)
    assert c.get_direct_subordinates()[0] is c1
    assert c1.get_superior() is c


def test_get_citizen1() -> None:
    c5 = Citizen(5, 'Citizen 5', 3005, 'Farmer', 101)
    who = c5.get_citizen(7)
    assert who is None


def test_get_citizen() -> None:
    c5 = Citizen(5, 'Citizen 5', 3005, 'Farmer', 101)
    who = c5.get_citizen(5)
    assert [who.cid, who.manufacturer, who.model_year, who.job, who.rating] == \
           [5, 'Citizen 5', 3005, 'Farmer', 101]


def test_get_citizen_one() -> None:
    c5 = Citizen(5, 'Citizen 5', 3005, 'Farmer', 101)
    who = c5.get_citizen(5)
    assert who is c5


def test_get_citizen_1() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c1.become_subordinate_to(c2)
    c2.become_subordinate_to(c3)
    assert c3.get_citizen(3) is c3
    assert c3.get_citizen(1) is c1
    assert c3.get_citizen(4) is None
    assert c2.get_citizen(1) is c1
    assert c2.get_citizen(3) is None


def test_get_citizen_2() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c1.become_subordinate_to(c2)
    c3.become_subordinate_to(c2)
    assert c2.get_direct_subordinates()[0] is c1
    assert c2.get_direct_subordinates()[1] is c3
    assert c2.get_citizen(3) is c3


def test_get_citizen_3() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c1.become_subordinate_to(c2)
    c3.become_subordinate_to(c2)
    assert c2.get_direct_subordinates()[0] is c1
    assert c2.get_direct_subordinates()[1] is c3
    assert c2.get_citizen(55) is None


def test_society_get_citizen_1() -> None:
    s = sample_society0()
    who = s.get_citizen(8)
    assert [who.cid, who.manufacturer, who.model_year, who.job, who.rating] == \
           [8, 'Citizen 8', 3008, 'Farmer', 22]


def test_society_get_citizen() -> None:
    s = Society()
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    s.add_citizen(c1)
    assert s.get_citizen(1) is c1
    assert s.get_citizen(2) is None


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


def test_get_all_subordinates_1() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    assert c1.get_all_subordinates() == []


def test_get_all_subordinates_no_sub() -> None:
    c1 = Citizen(10, "Starky Industries", 3024, "Labourer", 50)
    assert c1.get_all_subordinates() == []


def test_get_all_subordinates_doctest() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c1.become_subordinate_to(c2)
    c2.become_subordinate_to(c3)
    assert c3.get_all_subordinates()[0].cid == 1
    assert c3.get_all_subordinates()[1].cid == 2


def test_get_society_head() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c1.become_subordinate_to(c2)
    c2.become_subordinate_to(c3)
    head = c1.get_society_head()
    assert head is c3


def test_get_society_head_1() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c1.become_subordinate_to(c2)
    c2.become_subordinate_to(c3)
    head = c1.get_society_head()
    head1 = c2.get_society_head()
    assert head is c3
    assert head1 is c3


def test_get_society_head_only_head() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    head = c1.get_society_head()
    assert head is c1


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


def test_get_closest_common_superior_1() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    assert c1.get_closest_common_superior(1) == c1


def test_get_closest_common_superior_2() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c1.become_subordinate_to(c2)
    assert c1.get_closest_common_superior(2) == c2
    assert c2.get_closest_common_superior(1) == c2


def test_get_closest_common_superior_3() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c1.become_subordinate_to(c2)
    c3.become_subordinate_to(c2)
    assert c1.get_closest_common_superior(3) == c2
    assert c3.get_closest_common_superior(1) == c2


def test_get_closest_common_superior_4() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c1.become_subordinate_to(c2)
    c3.become_subordinate_to(c1)
    assert c3.get_closest_common_superior(1) == c1


def test_get_closest_common_superior_citizen_sup_cid_sub() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c4 = Citizen(4, "Starky Industries", 3022, "Manager", 55)
    c5 = Citizen(5, "Hookins National Lab", 3023, "Engineer", 50)
    c1.become_subordinate_to(c2)
    c2.become_subordinate_to(c3)
    c4.become_subordinate_to(c3)
    c5.become_subordinate_to(c4)
    assert c2.get_closest_common_superior(1) == c2


def test_get_closest_common_superior_cid_superior_citizen_sub() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c4 = Citizen(4, "Starky Industries", 3022, "Manager", 55)
    c5 = Citizen(5, "Hookins National Lab", 3023, "Engineer", 50)
    c1.become_subordinate_to(c2)
    c2.become_subordinate_to(c3)
    c4.become_subordinate_to(c3)
    c5.become_subordinate_to(c4)
    assert c1.get_closest_common_superior(3) == c3


def test_get_closest_common_superior_test() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c4 = Citizen(4, "Starky Industries", 3022, "Manager", 55)
    c5 = Citizen(5, "Hookins National Lab", 3023, "Engineer", 50)
    c2.become_subordinate_to(c1)
    c4.become_subordinate_to(c1)
    c3.become_subordinate_to(c2)
    c5.become_subordinate_to(c2)
    assert c3.get_closest_common_superior(5) == c2
    assert c5.get_closest_common_superior(3) == c2
    assert c3.get_closest_common_superior(4) == c1
    assert c4.get_closest_common_superior(3) == c1
    assert c3.get_closest_common_superior(2) == c2
    assert c2.get_closest_common_superior(3) == c2

    assert c1.get_closest_common_superior(1) == c1
    assert c2.get_closest_common_superior(2) == c2
    assert c3.get_closest_common_superior(3) == c3
    assert c4.get_closest_common_superior(4) == c4
    assert c5.get_closest_common_superior(5) == c5


def test_get_closest_common_superior_piazza() -> None:
    c3 = Citizen(3, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c10 = Citizen(10, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c4 = Citizen(4, "Starky Industries", 3022, "Manager", 55)
    c8 = Citizen(8, "Hookins National Lab", 3023, "Engineer", 50)
    c9 = Citizen(9, "Hookins National Lab", 3023, "Engineer", 50)
    c5 = Citizen(5, "Hookins National Lab", 3023, "Engineer", 50)
    c6 = Citizen(6, "Hookins National Lab", 3023, "Engineer", 50)
    c7 = Citizen(7, "Hookins National Lab", 3023, "Engineer", 50)
    c11 = Citizen(11, "Hookins National Lab", 3023, "Engineer", 50)
    c12 = Citizen(12, "Hookins National Lab", 3023, "Engineer", 50)
    c2.become_subordinate_to(c3)
    c10.become_subordinate_to(c3)
    c4.become_subordinate_to(c3)
    c8.become_subordinate_to(c2)
    c9.become_subordinate_to(c2)
    c5.become_subordinate_to(c4)
    c6.become_subordinate_to(c4)
    c7.become_subordinate_to(c4)
    c11.become_subordinate_to(c6)
    c12.become_subordinate_to(c6)
    assert c12.get_closest_common_superior(4) is c4
    assert c4.get_closest_common_superior(12) is c4


def test_get_closest_common_superior_v1() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c4 = Citizen(4, "Starky Industries", 3022, "Manager", 55)
    c5 = Citizen(5, "Hookins National Lab", 3023, "Engineer", 50)
    c1.become_subordinate_to(c2)
    c2.become_subordinate_to(c3)
    c4.become_subordinate_to(c3)
    c5.become_subordinate_to(c4)
    assert c1.get_closest_common_superior(5) == c3


def test_get_closest_common_superior_v2() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c4 = Citizen(4, "Starky Industries", 3022, "Manager", 55)
    c5 = Citizen(5, "Hookins National Lab", 3023, "Engineer", 50)
    c1.become_subordinate_to(c2)
    c2.become_subordinate_to(c3)
    c4.become_subordinate_to(c3)
    c5.become_subordinate_to(c4)
    assert c1.get_closest_common_superior(2) == c2


def test_get_closest_common_superior_v3() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c4 = Citizen(4, "Starky Industries", 3022, "Manager", 55)
    c5 = Citizen(5, "Hookins National Lab", 3023, "Engineer", 50)
    c1.become_subordinate_to(c2)
    c3.become_subordinate_to(c2)
    c2.become_subordinate_to(c4)
    c5.become_subordinate_to(c4)
    assert c1.get_closest_common_superior(3) == c2


def test_get_closest_common_superior_v4() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c4 = Citizen(4, "Starky Industries", 3022, "Manager", 55)
    c5 = Citizen(5, "Hookins National Lab", 3023, "Engineer", 50)
    c1.become_subordinate_to(c2)
    c3.become_subordinate_to(c2)
    c2.become_subordinate_to(c4)
    c5.become_subordinate_to(c4)
    assert c1.get_closest_common_superior(5) == c4

###########################################################################
# Tests for methods in Task 1.3
###########################################################################


def test_society_get_citizen() -> None:
    s = sample_society0()
    who = s.get_citizen(5)
    assert [who.cid, who.manufacturer, who.model_year, who.job, who.rating] == \
           [5, 'Citizen 5', 3005, 'Farmer', 101]


def test_society_get_citizen_empty() -> None:
    s = sample_society9()
    assert s.get_head() is None
    assert s.get_citizen(69) is None


def test_society_get_citizen_doesnt_exist_citizen() -> None:
    s = sample_society0()
    assert s.get_citizen(69) is None


def test_get_all_citizens() -> None:
    s = sample_society0()
    result = [c.cid for c in s.get_all_citizens()]
    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_get_all_citizens_empty() -> None:
    s = sample_society9()
    assert s.get_all_citizens() == []


def test_get_all_citizens_one_item() -> None:
    s = sample_society2()
    result = [c.cid for c in s.get_all_citizens()]
    assert result == [1]


def test_soc_get_all_citizens() -> None:
    o = Society()
    c1 = Citizen(1, "Starky Industries", 3024, "Manager", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 65)
    c3 = Citizen(3, "Starky Industries", 3024, "Labourer", 50)
    c4 = Citizen(4, "S.T.A.R.R.Y Lab", 3024, "Manager", 30)
    c5 = Citizen(5, "Hookins National Lab", 3024, "Labourer", 50)
    c6 = Citizen(6, "S.T.A.R.R.Y Lab", 3024, "Lawyer", 30)
    o.add_citizen(c4, None)
    o.add_citizen(c2, 4)
    o.add_citizen(c6, 2)
    o.add_citizen(c1, 4)
    o.add_citizen(c3, 1)
    o.add_citizen(c5, 1)
    assert o.get_all_citizens() == [c1, c2, c3, c4, c5, c6]
    assert [lol.cid for lol in o.get_all_citizens()] == [1, 2, 3, 4, 5, 6]
    h6 = Citizen(6, "S.T.A.R.R.Y Lab", 3024, "Lawyer", 30)
    q = Society(h6)
    assert q.get_all_citizens() == [q.get_citizen(6)]
    s = Society()
    c11 = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c21 = Citizen(2, 'Citizen 2', 3002, 'Bank robber', 19)
    c31 = Citizen(3, 'Citizen 3', 3003, 'Cook', 82)
    c41 = Citizen(4, 'Citizen 4', 3004, 'Cook', 5)
    c51 = Citizen(5, 'Citizen 5', 3005, 'Farmer', 100)
    s.add_citizen(c11)
    s.add_citizen(c21)
    s.add_citizen(c31)
    s.add_citizen(c41)
    s.add_citizen(c51)
    assert s._head.cid == 5
    assert s.get_all_citizens()[4].cid == 5


def test_add_citizen() -> None:
    s = Society()
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Some Lab", 3024, "Lawyer", 30)
    s.add_citizen(c2)
    s.add_citizen(c1, 2)
    assert s.get_head() == c2
    assert s.get_citizen(1) is c1
    assert c1.get_superior() is c2


def test_add_citizen_11() -> None:
    s = Society()
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Some Lab", 3024, "Lawyer", 30)
    c3 = Citizen(3, "Some Lab", 3024, "Lawyer", 30)
    s.add_citizen(c1)
    s.add_citizen(c3, 1)
    assert s.get_head() == c1
    s.add_citizen(c2)
    assert s.get_head() == c2
    assert len(c2.get_all_subordinates()) == 2
    assert c1 in c2.get_all_subordinates()
    assert c3 in c2.get_all_subordinates()
    assert c3 in c1.get_all_subordinates()


def test_add_citizen_1() -> None:
    s = Society()
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Some Lab", 3024, "Lawyer", 30)
    s.add_citizen(c1)
    s.add_citizen(c2)
    assert s.get_head() == c2
    assert c1 in c2.get_all_subordinates()
    assert len(c2.get_all_subordinates()) == 1


def test_add_citizen_2() -> None:
    s = Society()
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Some Lab", 3024, "Lawyer", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c4 = Citizen(4, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    s.add_citizen(c1)
    s.add_citizen(c2)
    s.add_citizen(c3, 2)
    s.add_citizen(c4, 3)
    assert s.get_head() == c2
    assert c1 in c2.get_direct_subordinates() and \
           c3 in c2.get_direct_subordinates()
    assert len(c2.get_direct_subordinates()) == 2
    assert c4.get_superior() is c3
    assert c4 in c3.get_all_subordinates()
    assert len(c3.get_all_subordinates()) == 1


def test_add_citizen_4() -> None:
    s = Society()
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Some Lab", 3024, "Lawyer", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c4 = Citizen(4, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c5 = Citizen(5, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    s.add_citizen(c3)
    s.add_citizen(c2, 3)
    s.add_citizen(c4, 3)
    s.add_citizen(c1, 2)
    s.add_citizen(c5)
    assert s.get_head() is c5
    assert len(c5.get_direct_subordinates()) == 1
    assert c3 in c5.get_direct_subordinates()
    assert len(c5.get_all_subordinates()) == 4


def test_add_citizen_empty() -> None:
    s = Society()
    c2 = Citizen(2, "Some Lab", 3024, "Lawyer", 30)
    s.add_citizen(c2)
    assert s.get_head() == c2


def test_add_citizen_only_head() -> None:
    s = Society()
    c2 = Citizen(2, "Some Lab", 3024, "Lawyer", 30)
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    s.add_citizen(c2)
    s.add_citizen(c1)
    assert s.get_head() == c1
    assert s.get_head().get_direct_subordinates() == [c2]
    assert s.get_citizen(2).get_direct_subordinates() == []
    assert s.get_citizen(2).get_superior() == c1


def test_add_citizen_v2() -> None:
    """Tests that citizen """
    s = Society()
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Some Lab", 3024, "Lawyer", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Labourer", 55)
    c2.add_subordinate(c3)
    s.add_citizen(c1)
    s.add_citizen(c2)
    assert s.get_head() == c2
    assert s.get_citizen(1) is c1
    assert c1.get_superior() is c2
    assert c2.get_direct_subordinates() == [c1]


def test_add_citizen_v3() -> None:
    s = Society()
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Some Lab", 3024, "Lawyer", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Labourer", 55)
    c2.add_subordinate(c3)
    s.add_citizen(c1)
    s.add_citizen(c2, 1)
    assert s.get_head() == c1
    assert s.get_citizen(1) is c1
    assert c2.get_superior() is c1
    assert c2.get_direct_subordinates() == [c3]
    assert c1.get_direct_subordinates() == [c2]


def test_add_citizen_v4() -> None:
    s = Society()
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Some Lab", 3024, "Lawyer", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Labourer", 55)
    c1.add_subordinate(c3)
    s.add_citizen(c2)
    s.add_citizen(c1)
    assert s.get_head() == c1
    assert s.get_citizen(1) is c1
    assert c2.get_superior() is c1
    assert c2.get_direct_subordinates() == []
    assert c1.get_direct_subordinates() == [c2]


def test_get_citizens_with_job() -> None:
    s = sample_society0()
    result = [c.cid for c in s.get_citizens_with_job('Farmer')]
    assert result == [5, 8, 9]


def test_get_citizens_with_job_empty() -> None:
    s = sample_society9()
    assert s.get_citizens_with_job('meow') == []


def test_get_citizens_with_job_not_present() -> None:
    s = sample_society0()
    result = [c.cid for c in s.get_citizens_with_job('woof')]
    assert result == []


def test_get_citizens_with_job_1() -> None:
    s = sample_society0()
    result = [c.cid for c in s.get_citizens_with_job('xyz')]
    assert result == []


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


def test_get_district_citizens_only_head() -> None:
    c1 = DistrictLeader(1, 'Citizen 1', 3001, 'Big boss', 10, 'D1')
    assert c1.get_district_citizens() == [c1]


def test_get_district_citizens_head_1_sub() -> None:
    c1 = DistrictLeader(1, "Some Lab", 3024, "Commander", 65, "District A")
    c2 = Citizen(2, "Hookins National Lab", 3024, "Lawyer", 30)
    c2.become_subordinate_to(c1)
    assert c1.get_district_citizens() == [c1, c2]


def test_get_district_citizens_leaf_and_inside() -> None:
    c1 = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c2 = DistrictLeader(2, 'Citizen 2', 3002, 'Bank robber', 19, 'D2')
    c3 = Citizen(3, 'Citizen 3', 3003, 'Cook', 82)
    c4 = Citizen(4, 'Citizen 4', 3004, 'Cook', 5)
    c2.become_subordinate_to(c1)
    c3.become_subordinate_to(c1)
    c4.become_subordinate_to(c1)
    c5 = Citizen(5, 'Citizen 5', 3005, 'Farmer', 101)
    c6 = Citizen(6, 'Citizen 6', 3006, 'Coach', 56)
    c5.become_subordinate_to(c2)
    c6.become_subordinate_to(c2)
    c8 = Citizen(8, 'Citizen 8', 3008, 'Farmer', 22)
    c9 = Citizen(9, 'Citizen 9', 3009, 'Farmer', 22)
    c10 = Citizen(10, 'Citizen 10', 3010, 'Driver', 22)
    c8.become_subordinate_to(c6)
    c9.become_subordinate_to(c6)
    c10.become_subordinate_to(c6)
    c7 = DistrictLeader(7, 'Citizen 7', 3007, 'Builder', 58, 'D7')
    c7.become_subordinate_to(c4)
    assert c7.get_district_citizens() == [c7]
    assert c2.get_district_citizens() == [c2, c5, c6, c8, c9, c10]

###########################################################################
# Tests for methods in Task 2.2
###########################################################################


def test_get_district_name() -> None:
    s = sample_society1()
    who = s.get_citizen(10)
    result = who.get_district_name()
    assert result == 'D2'


def test_get_district_name_self_district_tree() -> None:
    s = sample_society1()
    who = s.get_citizen(2)
    result = who.get_district_name()
    assert result == 'D2'


def test_get_district_name_leaf_district() -> None:
    s = sample_society1()
    who = s.get_citizen(7)
    result = who.get_district_name()
    assert result == 'D7'


def test_get_district_name_no_immediate_but_present() -> None:
    s = sample_society1()
    who = s.get_citizen(1)
    result = who.get_district_name()
    assert result == ''


def test_get_district_name_no_district() -> None:
    s = sample_society0()
    who = s.get_citizen(10)
    result = who.get_district_name()
    assert result == ''


def test_rename_district() -> None:
    s = sample_society1()
    who = s.get_citizen(10)
    who.rename_district('D10')
    leader = s.get_citizen(2)
    assert leader.get_district_name() == 'D10'


def test_rename_district_self_district_leader() -> None:
    s = sample_society1()
    who = s.get_citizen(2)
    who.rename_district('D2NEW')
    leader = s.get_citizen(2)
    assert leader.get_district_name() == 'D2NEW'


def test_rename_district_self_leaf_district_leader() -> None:
    s = sample_society1()
    who = s.get_citizen(7)
    who.rename_district('D7NEW')
    leader = s.get_citizen(7)
    assert leader.get_district_name() == 'D7NEW'


def test_rename_district_name_no_immediate_but_present() -> None:
    s = sample_society1()
    who = s.get_citizen(1)
    who.rename_district('D1NEW')
    result = who.get_district_name()
    assert result == ''


def test_rename_district_no_district_leaders() -> None:
    s = sample_society0()
    s.get_citizen(10).rename_district('nothing')
    all_citizens = s.get_all_citizens()
    for citizen in all_citizens:
        assert isinstance(citizen, Citizen)
    assert s.get_head() == s.get_citizen(1)

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


def test_change_citizen_type_1() -> None:
    s = sample_society1()
    s.change_citizen_type(1, 'D1')
    who = s.get_citizen(1)
    assert isinstance(who, DistrictLeader)
    assert [who.cid, who.manufacturer, who.model_year, who.job, who.rating,
            who.get_district_name()] == [1, 'Citizen 1', 3001, 'Big boss', 10,
                                         'D1']
    assert s.get_head().cid == 1
    assert [c.cid for c in who.get_all_subordinates()] == [2, 3, 4, 5, 6, 7, 8,
                                                           9, 10]
    assert who.get_superior() is None


def test_change_citizen_type_2() -> None:
    s = Society()
    c1 = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    s.add_citizen(c1)
    s.change_citizen_type(1, 'D1')
    who = s.get_citizen(1)
    assert isinstance(who, DistrictLeader)
    assert [who.cid, who.manufacturer, who.model_year, who.job, who.rating,
            who.get_district_name()] == [1, 'Citizen 1', 3001, 'Big boss', 10,
                                         'D1']
    assert who.get_superior() is None
    assert who.get_all_subordinates() == []


def test_change_citizen_type_leaf_citizen() -> None:
    s = sample_society1()
    s.change_citizen_type(5, 'D5')
    who = s.get_citizen(5)
    assert isinstance(who, DistrictLeader)
    assert who.get_district_name() == 'D5'
    assert [c.cid for c in who.get_all_subordinates()] == []
    assert who.get_superior().cid == 2


def test_change_citizen_type_head_citizen() -> None:
    s = sample_society1()
    s.change_citizen_type(1, 'D1')
    who = s.get_citizen(1)
    assert isinstance(who, DistrictLeader)
    assert who.get_district_name() == 'D1'
    assert [c.cid for c in who.get_all_subordinates()] == [2, 3, 4]
    # assert who.get_superior().cid == 2

###########################################################################
# Tests for method in Task 3.1
###########################################################################


def test_swap_up_v1() -> None:
    s = Society()
    c1 = DistrictLeader(1, "Some Lab", 3024, "Commander", 65, "District A")
    c2 = Citizen(2, "Hookins National Lab", 3024, "Lawyer", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Labourer", 55)
    s.add_citizen(c1)
    s.add_citizen(c2, 1)
    s.add_citizen(c3, 2)
    c3 = s._swap_up(c3)
    assert c3.job == "Lawyer"
    assert isinstance(c3, Citizen)
    assert c3.cid == 3
    assert c3.rating == 55
    assert [c.cid for c in c3.get_all_subordinates()] == [2]


def test_swap_up_v2() -> None:
    s = Society()
    c1 = DistrictLeader(1, "Some Lab", 3024, "Commander", 65, "District A")
    c2 = Citizen(2, "Hookins National Lab", 3024, "Lawyer", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Labourer", 55)
    c4 = Citizen(4, "Starky Industries", 3022, "Manager", 55)
    s.add_citizen(c1)
    s.add_citizen(c2, 1)
    s.add_citizen(c3, 2)
    s.add_citizen(c4, 2)
    c3 = s._swap_up(c3)
    assert c3.job == "Lawyer"
    assert isinstance(c3, Citizen)
    assert c3.cid == 3
    assert c3.rating == 55
    assert [c.cid for c in c3.get_all_subordinates()] == [2, 4]


def test_swap_up_v3() -> None:
    s = Society()
    c1 = DistrictLeader(6, "Some Lab", 3024, "Commander", 65, "District A")
    c2 = Citizen(2, "Hookins National Lab", 3024, "Lawyer", 30)
    c3 = Citizen(10, "S.T.A.R.R.Y Lab", 3010, "Labourer", 55)
    c4 = Citizen(11, "Starky Industries", 3022, "Manager", 55)
    s.add_citizen(c1)
    s.add_citizen(c2, 6)
    s.add_citizen(c3, 2)
    s.add_citizen(c4, 2)
    c2 = s._swap_up(c2)

    assert [c.cid for c in c2.get_all_subordinates()] == [6, 10, 11]


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


def test_promote_citizen_to_head() -> None:
    s = promote_citizen_example()
    c = Citizen(20, 'Citizen 20', 3001, 'Watcher', 30)
    c1 = Citizen(21, 'Citizen 21', 3001, 'Watcher', 90)
    s.add_citizen(c, 6)
    s.add_citizen(c1, 20)
    s.promote_citizen(21)
    c = s.get_citizen(20)
    c1 = s.get_citizen(21)
    assert s.get_head() == c1
    assert c1.get_direct_subordinates() == [s.get_citizen(5), s.get_citizen(6)]


@given(height=integers(min_value=2, max_value=500))
def test_promote_citizen_up_ladder(height: int) -> None:
    s = Society()
    c = Citizen(1, 'Citizen clone', 31032, 'Clone', 1)
    s.add_citizen(c)
    for i in range(height - 1):
        c = Citizen(i + 2, 'Citizen clone', 31032, 'Clone', i + 2)
        s.add_citizen(c, i + 1)
    s.promote_citizen(height)
    assert s.get_head() == s.get_citizen(height)
    assert s.get_citizen(height).get_direct_subordinates() == [s.get_citizen(1)]
    for i in range(height - 2):
        assert s.get_citizen(i + 1).get_direct_subordinates() == \
               [s.get_citizen(i + 2)]


@given(height=integers(min_value=5, max_value=500))
def test_promote_citizen_up_ladder_stop_middle(height: int) -> None:
    s = Society()
    c = Citizen(1, 'Citizen clone', 31032, 'Clone', 1)
    s.add_citizen(c)
    midpoint = (height - 1)//2
    for i in range(height - 1):
        c = Citizen(i + 2, 'Citizen clone', 31032, 'Clone', i + 2)
        if i == midpoint - 2:
            c = DistrictLeader(i + 2, 'Leader', 31032, 'Clone', i + 2, 'A')
        s.add_citizen(c, i + 1)
    s.promote_citizen(height)
    assert s.get_head() == s.get_citizen(1)
    assert s.get_citizen(height).get_direct_subordinates() == \
           [s.get_citizen(midpoint)]
    assert isinstance(s.get_citizen(height), DistrictLeader)


def test_promote_citizen_v2() -> None:
    """Test promote_citizen on head"""
    s = Society()
    c1 = DistrictLeader(6, "Some Lab", 3024, "Commander", 65, "District A")
    c2 = Citizen(2, "Hookins National Lab", 3024, "Lawyer", 70)
    # c3 = Citizen(10, "S.T.A.R.R.Y Lab", 3010, "Labourer", 55)
    # c4 = Citizen(11, "Starky Industries", 3022, "Manager", 55)
    s.add_citizen(c1)
    s.add_citizen(c2, 6)
    s.promote_citizen(2)
    promoted = s.get_citizen(2)
    demoted = s.get_citizen(6)
    assert isinstance(promoted, DistrictLeader)
    assert promoted.get_superior() is None
    assert not isinstance(demoted, DistrictLeader)
    assert [c.cid for c in promoted.get_all_subordinates()] == [demoted.cid]
    assert [c.cid for c in demoted.get_all_subordinates()] == []
    assert demoted.get_superior() == promoted


def test_promote_citizen_v3() -> None:
    """Test promote_citizen on head"""
    s = Society()
    c1 = DistrictLeader(6, "Some Lab", 3024, "Commander", 65, "District A")
    c2 = Citizen(2, "Hookins National Lab", 3024, "Lawyer", 30)
    # c3 = Citizen(10, "S.T.A.R.R.Y Lab", 3010, "Labourer", 55)
    # c4 = Citizen(11, "Starky Industries", 3022, "Manager", 55)
    s.add_citizen(c1)
    s.add_citizen(c2, 6)
    s.promote_citizen(2)
    # 2 didn't promote
    promoted = s.get_citizen(2)
    demoted = s.get_citizen(6)
    assert isinstance(promoted, Citizen)
    assert promoted.get_superior() is demoted
    assert isinstance(demoted, Citizen)
    assert [c.cid for c in promoted.get_all_subordinates()] == []
    assert [c.cid for c in demoted.get_all_subordinates()] == [promoted.cid]
    assert demoted.get_superior() is None
###########################################################################
# Tests for method in Task 3.2
###########################################################################


def test_get_highest_rated_subordinate() -> None:
    s = sample_society1()
    who = s.get_citizen(2)
    result = who.get_highest_rated_subordinate()
    assert result.cid == 5


def test_get_highest_rated_subordinate_one_subordinate() -> None:
    s = Society()
    c = Citizen(1, 'Citizen 20', 3001, 'Watcher', 30)
    c1 = Citizen(2, 'Citizen 20', 3002, 'Dumb', 40)
    s.add_citizen(c)
    s.add_citizen(c1, 1)
    assert s.get_head().get_highest_rated_subordinate() == c1


def test_get_highest_rated_subordinate_rating_tie() -> None:
    s = Society()
    c = Citizen(1, 'Citizen 20', 3001, 'Watcher', 30)
    c1 = Citizen(2, 'Citizen 20', 3002, 'Dumb', 40)
    c2 = Citizen(3, 'Citizen 20', 3002, 'Dumb', 40)
    c3 = Citizen(4, 'Citizen 20', 3002, 'Dumb', 30)
    s.add_citizen(c)
    s.add_citizen(c1, 1)
    s.add_citizen(c2, 1)
    s.add_citizen(c3, 1)
    assert s.get_head().get_highest_rated_subordinate() == c1


def test_get_highest_rated_subordinate_v2() -> None:
    s = Society()
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    s.add_citizen(c)
    s.add_citizen(c1, 1)
    assert c.get_highest_rated_subordinate().cid == 11


def test_get_highest_rated_subordinate_v3() -> None:
    s = Society()
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', -1)
    s.add_citizen(c)
    s.add_citizen(c1, 1)
    assert c.get_highest_rated_subordinate().cid == 11


def test_get_highest_rated_subordinate_v4() -> None:
    s = Society()
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 0)
    s.add_citizen(c)
    s.add_citizen(c1, 1)
    assert c.get_highest_rated_subordinate().cid == 11


def test_get_highest_rated_subordinate_v5() -> None:
    s = Society()
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 0)
    c2 = Citizen(12, 'Citizen 11', 3011, 'Watcher', 0)
    s.add_citizen(c)
    s.add_citizen(c1, 1)
    s.add_citizen(c2, 1)
    assert c.get_highest_rated_subordinate().cid == 11


def test_get_highest_rated_subordinate_v6() -> None:
    s = Society()
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 2)
    c2 = Citizen(12, 'Citizen 11', 3011, 'Watcher', 4)
    s.add_citizen(c)
    s.add_citizen(c1, 1)
    s.add_citizen(c2, 1)
    assert c.get_highest_rated_subordinate().cid == 12


def test_delete_citizen() -> None:
    s = sample_society1()
    s.delete_citizen(6)
    who = s.get_citizen(2)
    assert [c.cid for c in who.get_direct_subordinates()] == [5, 8, 9, 10]
    assert s.get_citizen(6) is None


def test_delete_citizen_only_head() -> None:
    s = sample_society2()
    s.delete_citizen(1)
    assert s.get_head() == None
    assert s.get_citizen(1) is None


def test_delete_citizen_only_head_is_district() -> None:
    s = sample_society3()
    s.delete_citizen(1)
    assert s.get_head() == None
    assert s.get_citizen(1) is None


def test_delete_citizen_only_head_1_head_1_sub_both_citizens() -> None:
    s = sample_society4()
    s.delete_citizen(1)
    who = s.get_citizen(2)
    assert [c.cid for c in who.get_direct_subordinates()] == []
    assert s.get_head().cid == 2
    assert s.get_citizen(1) is None


def test_delete_citizen_only_head_1_head_1_sub_both_district() -> None:
    s = sample_society5()
    s.delete_citizen(1)
    who = s.get_citizen(2)
    assert [c.cid for c in who.get_direct_subordinates()] == []
    assert s.get_head().cid == 2
    assert s.get_citizen(1) is None


def test_delete_citizen_only_head_sub_district_head_citizen() -> None:
    s = sample_society6()
    s.delete_citizen(1)
    who = s.get_citizen(2)
    assert [c.cid for c in who.get_direct_subordinates()] == []
    assert s.get_head().cid == 2
    assert s.get_citizen(1) is None


def test_delete_citizen_only_head_sub_citizen_head_district() -> None:
    s = sample_society7()
    s.delete_citizen(1)
    who = s.get_citizen(2)
    assert [c.cid for c in who.get_direct_subordinates()] == []
    assert s.get_head().cid == 2
    assert s.get_citizen(1) is None


def test_delete_citizen_end() -> None:
    s = sample_society1()
    s.delete_citizen(8)
    who = s.get_citizen(6)
    assert [c.cid for c in who.get_direct_subordinates()] == [9, 10]
    assert s.get_citizen(8) is None


def test_delete_citizen_head_highest_rated_no_subordinate_or_d_leader() -> None:
    s = sample_society1()
    s.delete_citizen(1)
    who = s.get_citizen(3)
    assert [c.cid for c in who.get_direct_subordinates()] == [2, 4]
    assert s.get_citizen(1) is None


def test_delete_citizen_1() -> None:
    s = Society()
    c1 = Citizen(1, 'Citizen 1', 3001, 'Watcher', 10)
    s.add_citizen(c1)
    s.delete_citizen(1)
    assert s.get_head() is None


def test_delete_citizen_2() -> None:
    s = Society()
    c1 = Citizen(1, 'Citizen 1', 3001, 'Watcher', 10)
    s.add_citizen(c1)
    c2 = DistrictLeader(2, 'Citizen 2', 3002, 'Bank robber', 19, 'D2')
    c3 = Citizen(3, 'Citizen 3', 3003, 'Cook', 82)
    s.add_citizen(c2, 1)
    s.add_citizen(c3, 1)
    s.delete_citizen(1)
    assert s.get_head() is c3
    assert c2 in s.get_head().get_all_subordinates()


def test_delete_citizen_3() -> None:
    s = Society()
    c1 = Citizen(1, 'Citizen 1', 3001, 'Watcher', 10)
    s.add_citizen(c1)
    c2 = DistrictLeader(2, 'Citizen 2', 3002, 'Bank robber', 19, 'D2')
    s.add_citizen(c2, 1)
    s.delete_citizen(1)
    assert s.get_head() is c2
    assert s.get_head().get_all_subordinates() == []


def test_delete_citizen_4() -> None:
    s = Society()
    c1 = Citizen(1, 'Citizen 1', 3001, 'Watcher', 10)
    s.add_citizen(c1)
    c2 = DistrictLeader(2, 'Citizen 2', 3002, 'Bank robber', 19, 'D2')
    c3 = Citizen(3, 'Citizen 3', 3003, 'Cook', 82)
    c4 = Citizen(4, 'Citizen 4', 3004, 'Cook', 5)
    c5 = Citizen(5, 'Citizen 5', 3005, 'Farmer', 101)
    c6 = Citizen(6, 'Citizen 6', 3006, 'Coach', 56)
    s.add_citizen(c2, 1)
    s.add_citizen(c3, 1)
    s.add_citizen(c4, 2)
    s.add_citizen(c5, 3)
    s.add_citizen(c6, 3)
    s.delete_citizen(1)
    assert s.get_head() is c3
    assert [x.cid for x in s.get_head().get_direct_subordinates()] == [2, 5, 6]


def test_delete_citizen_21() -> None:
    s = Society()
    c1 = Citizen(1, 'Citizen 1', 3001, 'Watcher', 10)
    s.add_citizen(c1)
    c2 = DistrictLeader(2, 'Citizen 2', 3002, 'Bank robber', 19, 'D2')
    c3 = Citizen(3, 'Citizen 3', 3003, 'Cook', 82)
    s.add_citizen(c2, 1)
    s.add_citizen(c3, 1)
    s.delete_citizen(2)
    assert s.get_head() is c1
    assert [x.cid for x in s.get_head().get_all_subordinates()] == [3]


def test_delete_citizen_31() -> None:
    s = Society()
    c1 = Citizen(1, 'Citizen 1', 3001, 'Watcher', 10)
    s.add_citizen(c1)
    c2 = DistrictLeader(2, 'Citizen 2', 3002, 'Bank robber', 19, 'D2')
    s.add_citizen(c2, 1)
    s.delete_citizen(2)
    assert s.get_head() is c1
    assert s.get_head().get_all_subordinates() == []


def test_delete_citizen_41() -> None:
    s = Society()
    c1 = Citizen(1, 'Citizen 1', 3001, 'Watcher', 10)
    s.add_citizen(c1)
    c2 = DistrictLeader(2, 'Citizen 2', 3002, 'Bank robber', 19, 'D2')
    c3 = Citizen(3, 'Citizen 3', 3003, 'Cook', 82)
    c4 = Citizen(4, 'Citizen 4', 3004, 'Cook', 5)
    c5 = Citizen(5, 'Citizen 5', 3005, 'Farmer', 101)
    c6 = Citizen(6, 'Citizen 6', 3006, 'Coach', 56)
    s.add_citizen(c2, 1)
    s.add_citizen(c3, 1)
    s.add_citizen(c4, 2)
    s.add_citizen(c5, 3)
    s.add_citizen(c6, 3)
    s.delete_citizen(3)
    assert [x.cid for x in s.get_head().get_direct_subordinates()] == [2, 5, 6]
    s.delete_citizen(4)
    assert [x.cid for x in s.get_head().get_direct_subordinates()] == [2, 5, 6]
    assert c2.get_all_subordinates() == []


def test_delete_only_citizen() -> None:
    s = Society()
    c = Citizen(1, 'Citizen 20', 3001, 'Watcher', 30)
    s.add_citizen(c)
    s.delete_citizen(1)
    assert s.get_all_citizens() == []
    assert s.get_head() is None


def test_delete_head_citizen_1() -> None:
    s = sample_society1()
    s.delete_citizen(1)
    assert s.get_head() == s.get_citizen(3)
    all_citizens = s.get_citizen(3).get_all_subordinates()
    all_citizens.insert(1, s.get_citizen(3))
    assert s.get_all_citizens() == all_citizens
    assert [subordinate.cid
            for subordinate in s.get_head().get_direct_subordinates()] == [2, 4]


def test_delete_head_citizen_2() -> None:
    s = sample_society1()
    s.get_citizen(2).rating = 100
    s.delete_citizen(1)
    assert s.get_head() == s.get_citizen(2)
    all_citizens = s.get_citizen(2).get_all_subordinates()
    all_citizens.insert(0, s.get_citizen(2))
    assert s.get_all_citizens() == all_citizens
    assert [subordinate.cid for subordinate
            in s.get_head().get_direct_subordinates()] == [3, 4, 5, 6]


# def test_delete_citizen_head_highest_rated_yes_subordinate_no_d_leader() -> None:
#     s = sample_society4()
#     s.delete_citizen(1)
#     who = s.get_citizen(4)
#     assert [c.cid for c in who.get_direct_subordinates()] == [2, 3, 7]
#     assert s.get_citizen(1) is None


def test_piazza() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Manager", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 65)
    c3 = Citizen(3, "Starky Industries", 3024, "Labourer", 50)
    c4 = DistrictLeader(4, "S.T.A.R.R.Y Lab", 3024, "Manager", 60, 'd')
    c5 = Citizen(5, "Hookins National Lab", 3024, "Labourer", 80)
    c6 = Citizen(6, "S.T.A.R.R.Y Lab", 3024, "Lawyer", 70)
    o = Society(c4)
    o.add_citizen(c2, 4)
    o.add_citizen(c6, 2)
    o.add_citizen(c1, 4)
    o.add_citizen(c3, 1)
    o.add_citizen(c5, 1)
    o.promote_citizen(6)
    assert isinstance(o.get_citizen(6), DistrictLeader)
    assert not isinstance(o.get_citizen(4), DistrictLeader)


if __name__ == '__main__':
    import pytest

    pytest.main(['a2_sample_test_3.py'])

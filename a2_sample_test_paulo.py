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


def sample_society2() -> Society:
    """Return a society"""
    s = Society()
    head = Citizen(1, "C1", 3001, "Num1", 20)
    s.add_citizen(head)
    a1 = Citizen(2, "a1", 3001, "Num2", 30)
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


def test_add_subordinate_asc() -> None:
    """Test that add_subordinate maintains ascending order of cid"""
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c2 = Citizen(8, 'Citizen 11', 3011, 'Watcher', 25)
    c3 = Citizen(7, 'Citizen 11', 3011, 'Watcher', 25)
    c4 = Citizen(9, 'Citizen 11', 3011, 'Watcher', 25)
    c.add_subordinate(c1)
    c.add_subordinate(c2)
    c.add_subordinate(c3)
    c.add_subordinate(c4)
    assert c.get_direct_subordinates() == [c3, c2, c4, c1]


def test_add_subordinate_multiple() -> None:
    """Test that add_subordinate works with multiple adds"""
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c2 = Citizen(8, 'Citizen 11', 3011, 'Watcher', 25)
    c3 = Citizen(7, 'Citizen 11', 3011, 'Watcher', 25)
    c4 = Citizen(9, 'Citizen 11', 3011, 'Watcher', 25)
    c.add_subordinate(c1)
    c.add_subordinate(c2)
    c.add_subordinate(c3)
    c.add_subordinate(c4)
    assert c.get_direct_subordinates() == [c3, c2, c4, c1]
    assert c1.get_superior() == c
    assert c2.get_superior() == c
    assert c3.get_superior() == c
    assert c4.get_superior() == c


def test_add_subordinate_no_super() -> None:
    """Test that add_subordinate works when the new subordinate has no
    super"""
    s = sample_society1()
    c11 = Citizen(11, 'Citizen 11', 3010, 'Driver', 22)
    c3 = s.get_citizen(3)
    c3.add_subordinate(c11)
    assert c3.get_direct_subordinates() == [c11]
    assert c11.get_superior() == c3


def test_remove_subordinate() -> None:
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c.add_subordinate(c1)
    c.remove_subordinate(11)
    assert c.get_direct_subordinates() == []
    assert c1.get_superior() is None


def test_remove_subordinate_grandchildren() -> None:
    """Test that a subordinate's grandchildren are removed from this
    society if its parent is removed"""
    s = sample_society1()
    c1 = s.get_citizen(1)
    c2 = s.get_citizen(2)
    c5 = s.get_citizen(5)
    c6 = s.get_citizen(6)
    c8 = s.get_citizen(8)
    c9 = s.get_citizen(9)
    c10 = s.get_citizen(10)
    c1.remove_subordinate(2)
    all_subs = s.get_all_citizens()
    assert c5 not in all_subs
    assert c6 not in all_subs
    assert c8 not in all_subs
    assert c9 not in all_subs
    assert c10 not in all_subs
    assert c2.get_direct_subordinates() == [c5, c6]
    assert c2.get_all_subordinates() == [c5, c6, c8, c9, c10]
    assert c5.get_superior() == c2
    assert c6.get_superior() == c2
    assert c5.get_direct_subordinates() == []
    assert c6.get_direct_subordinates() == [c8, c9, c10]
    assert c8.get_superior() == c6
    assert c9.get_superior() == c6
    assert c10.get_superior() == c6


def test_become_subordinate_to() -> None:
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c1.become_subordinate_to(c)
    assert c.get_direct_subordinates()[0] is c1
    assert c1.get_superior() is c


def test_become_subordinate_head_to_none() -> None:
    """Test that nothing changes if become_subordinate to is called
    on head with a  None superior"""
    s = sample_society1()
    c1 = s.get_citizen(1)
    old_direct_subs = c1.get_direct_subordinates()
    old_head = s.get_head()
    old_all_subs = c1.get_all_subordinates()
    c1.become_subordinate_to(None)
    assert old_head == s.get_head()
    assert old_direct_subs == c1.get_direct_subordinates()
    assert old_all_subs == c1.get_all_subordinates()


def test_get_citizen() -> None:
    c5 = Citizen(5, 'Citizen 5', 3005, 'Farmer', 101)
    who = c5.get_citizen(5)
    assert [who.cid, who.manufacturer, who.model_year, who.job, who.rating] == \
           [5, 'Citizen 5', 3005, 'Farmer', 101]


def test_get_citizen_head() -> None:
    """Test get_citizen on the head of a society"""
    s = sample_society1()
    c1 = s.get_citizen(1)
    citizen = c1.get_citizen(4)
    assert citizen == s.get_citizen(4)


def test_get_citizen_deep() -> None:
    """Test get_citizen when it is deep in the hierarchy"""
    s = sample_society1()
    c2 = s.get_citizen(2)
    citizen = c2.get_citizen(9)
    c9 = s.get_citizen(9)
    assert citizen == c9


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


def test_get_all_subordinates_none() -> None:
    """Test that get_all_subordinates returns an empty list if this citizen
    has no subordinates"""
    s = sample_society1()
    c3 = s.get_citizen(3)
    subordinates = c3.get_all_subordinates()
    assert subordinates == []


def test_get_all_subordinates_direct() -> None:
    """Test that get_all_subordinates only returns direct subordinates
    if their subordinates don't have subordinates"""
    s = sample_society1()
    c6 = s.get_citizen(6)
    subordinates = c6.get_all_subordinates()
    assert subordinates == c6.get_direct_subordinates()


def test_get_all_subordinates_head() -> None:
    """Test that get_all_subordinates returns all citizens - head if called
    on the head"""
    s = sample_society1()
    c1 = s.get_citizen(1)
    subordinates = c1.get_all_subordinates()
    citizens = s.get_all_citizens()
    citizens.remove(c1)
    assert citizens == subordinates


def test_get_society_head() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c1.become_subordinate_to(c2)
    c2.become_subordinate_to(c3)
    head = c1.get_society_head()
    assert head is c3


def test_get_society_head_head() -> None:
    """Test that get_society_head returns self if self is the head"""
    s = sample_society1()
    c1 = s.get_citizen(1)
    head = c1.get_society_head()
    assert head == c1


def test_get_society_head_lower() -> None:
    """Test that get_society_head returns the right head if self is low
    on the hierarchy"""
    s = sample_society1()
    c1 = s.get_citizen(1)
    c9 = s.get_citizen(9)
    head = c9.get_society_head()
    assert head == c1


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


def test_get_closest_common_superior_higher() -> None:
    """Test this method when the self is higher than the other citizen"""
    s = sample_society1()
    c5 = s.get_citizen(5)
    assert c5.get_closest_common_superior(10) == s.get_citizen(2)


def test_get_closest_common_superior_lower() -> None:
    """Test this method when the self is lower than the other citizen"""
    s = sample_society1()
    c10 = s.get_citizen(10)
    assert c10.get_closest_common_superior(5) == s.get_citizen(2)


def test_get_closest_common_superior_same() -> None:
    """Test this method when the self is on the same level as the other
    citizen"""
    s = sample_society1()
    c5 = s.get_citizen(5)
    assert c5.get_closest_common_superior(7) == s.get_citizen(1)


def test_get_closest_common_superior_siblings() -> None:
    """Test this method when the self and other are subs of the same super"""
    s = sample_society1()
    c8 = s.get_citizen(8)
    assert c8.get_closest_common_superior(10) == s.get_citizen(6)


def test_get_closest_common_superior_equal() -> None:
    """Test this method when the self and other are the same citizen"""
    s = sample_society1()
    c10 = s.get_citizen(10)
    assert c10.get_closest_common_superior(10) == s.get_citizen(10)


def test_get_closest_common_superior_superior() -> None:
    """Test this method when the self is the superior of other"""
    s = sample_society1()
    c6 = s.get_citizen(6)
    assert c6.get_closest_common_superior(10) == s.get_citizen(6)


###########################################################################
# Tests for methods in Task 1.3
###########################################################################

def test_society_get_citizen() -> None:
    s = sample_society0()
    who = s.get_citizen(5)
    assert [who.cid, who.manufacturer, who.model_year, who.job, who.rating] == \
           [5, 'Citizen 5', 3005, 'Farmer', 101]


def test_society_get_citizen_empty() -> None:
    """ Test that this method returns None if the society is empty"""
    s = Society()
    assert s.get_citizen(1) is None


def test_society_get_citizen_dne() -> None:
    """ Test that this method returns None if this citizen isn't in
    this society"""
    s = sample_society1()
    assert s.get_citizen(23) is None


def test_society_get_citizen_head() -> None:
    """Test that this method returns the head if cid is cid of head"""
    s = sample_society1()
    assert s.get_citizen(1) == s.get_head()


def test_get_all_citizens() -> None:
    s = sample_society0()
    result = [c.cid for c in s.get_all_citizens()]
    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_get_all_citizens_empty() -> None:
    """Test that this method returns None in an empty society"""
    s = Society()
    assert s.get_all_citizens() == []


def test_get_all_citizens_head() -> None:
    """Test that this method returns the head when only one citizen exists"""
    s = Society(Citizen(1, 'Citizen 1', 3001, 'Watcher', 10))
    c1 = s.get_citizen(1)
    assert s.get_all_citizens() == [c1]


def test_get_all_citizens_asc() -> None:
    """Test that this method maintains ascending order of cids"""
    s = sample_society1()
    all = s.get_all_citizens()
    assert all == [s.get_citizen(1), s.get_citizen(2), s.get_citizen(3),
                   s.get_citizen(4), s.get_citizen(5), s.get_citizen(6),
                   s.get_citizen(7), s.get_citizen(8), s.get_citizen(9),
                   s.get_citizen(10)]


def test_add_citizen() -> None:
    s = Society()
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Some Lab", 3024, "Lawyer", 30)
    s.add_citizen(c2)
    s.add_citizen(c1, 2)
    assert s.get_head() == c2
    assert s.get_citizen(1) is c1
    assert c1.get_superior() is c2


def test_add_citizen_new_head() -> None:
    """Test that this method makes this citizen the new head with the old
    head the only direct subordinate"""
    s = sample_society1()
    new = Citizen(11, "New Head", 3000, "King", 100)
    subordinates = s.get_all_citizens()
    s.add_citizen(new)
    assert s.get_head() == new
    assert new.get_all_subordinates() == subordinates
    assert new.get_direct_subordinates() == [s.get_citizen(1)]


def test_add_citizen_subs() -> None:
    """Test that the citizen's subordinates get added when it gets added
    to the society"""
    s = sample_society1()
    new = Citizen(11, "New Head", 3000, "King", 100)
    sub = Citizen(12, "Underling", 3001, "Squire", 99)
    sub.become_subordinate_to(new)
    subordinates = s.get_all_citizens()
    s.add_citizen(new)
    subordinates = merge(subordinates, [sub])
    assert s.get_head() == new
    assert new.get_all_subordinates() == subordinates
    assert new.get_direct_subordinates() == [s.get_citizen(1), sub]


def test_add_citizen_norm() -> None:
    """Test that adding this citizen normally works"""
    s = sample_society1()
    new = Citizen(11, "Guy", 3000, "Guy", 100)
    citizens = s.get_all_citizens()
    s.add_citizen(new, 4)
    citizens = merge(citizens, [new])
    assert new.get_superior() == s.get_citizen(4)
    assert s.get_citizen(4).get_direct_subordinates() == [s.get_citizen(7), new]
    assert s.get_all_citizens() == citizens


def test_add_citizen_new_head() -> None:
    """Test that this method adds a new head with the old head being the only direct sub"""
    s = sample_society1()
    c = Citizen(11, "Manufacturer", 3000, "Job", 10)
    s.add_citizen(c)
    assert s.get_head() == c
    assert c.get_direct_subordinates() == [s.get_citizen(1)]
    assert s.get_citizen(1).get_direct_subordinates() == [s.get_citizen(2), s.get_citizen(3), s.get_citizen(4)]


def test_get_citizens_with_job() -> None:
    s = sample_society0()
    result = [c.cid for c in s.get_citizens_with_job('Farmer')]
    assert result == [5, 8, 9]


def test_get_citizens_with_job_dne() -> None:
    """Test that this method returns an empty list if no one has this job"""
    s = sample_society1()
    assert s.get_citizens_with_job("Paulo") == []


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


def test_get_district_citizens_single() -> None:
    """Test this method when there is only one citizen in this district"""
    s = sample_society1()
    c7 = s.get_citizen(7)
    assert c7.get_district_citizens() == [c7]


###########################################################################
# Tests for methods in Task 2.2
###########################################################################


def test_get_district_name() -> None:
    s = sample_society1()
    who = s.get_citizen(10)
    result = who.get_district_name()
    assert result == 'D2'


def test_get_district_name_cit() -> None:
    """Test that this method returns its superior's district"""
    s = sample_society1()
    c9 = s.get_citizen(9)
    assert c9.get_district_name() == "D2"


def test_get_district_name_cit_none() -> None:
    """Test that this method returns empty string if citizen isn't part
    of a district"""
    s = sample_society1()
    c4 = s.get_citizen(4)
    assert c4.get_district_name() == ""


def test_get_district_name_cit_none_head() -> None:
    """Test that this method returns empty string if citizen isn't part
    of a district"""
    s = sample_society1()
    c1 = s.get_citizen(1)
    assert c1.get_district_name() == ""


def test_get_district_name_dl() -> None:
    """Test that this method returns the district this DL leads"""
    s = sample_society1()
    c2 = s.get_citizen(2)
    assert c2.get_district_name() == "D2"


def test_get_district_name_dl_multi() -> None:
    """Test that this method returns the closest district if it has
    superiors who are DL's"""
    s = sample_society1()
    s.change_citizen_type(1, "D1")
    c2 = s.get_citizen(2)
    assert c2.get_district_name() == "D2"


def test_rename_district() -> None:
    s = sample_society1()
    who = s.get_citizen(10)
    who.rename_district('D10')
    leader = s.get_citizen(2)
    assert leader.get_district_name() == 'D10'


def test_rename_district_cit_none() -> None:
    """Test that this method does nothing if they are not part of a district"""
    s = sample_society1()
    c4 = s.get_citizen(4)
    c4.rename_district("D4")
    assert c4.get_district_name() == ""
    assert s.get_citizen(7).get_district_name() == "D7"
    assert s.get_citizen(1).get_district_name() == ""


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


def test_change_citizen_type_dl() -> None:
    """Test change_citizen_type creates a new citizen who is a
    district leader with the same attributes"""
    s = sample_society1()
    c8 = Citizen(8, 'Citizen 8', 3001, 'Watcher', 10)
    s.add_citizen(c8, 7)
    s.change_citizen_type(4, "District 7")
    who = s.get_citizen(4)
    print(s)
    assert isinstance(who, Citizen)
    assert who.get_superior() == s.get_citizen(1)
    assert who.get_direct_subordinates() == [s.get_citizen(7)]
    assert who.get_district_name() == "District 7"


def test_change_citizen_type_old_c() -> None:
    """Test that this method removes the old citizen from the heirarchy"""
    s = sample_society1()
    old = s.get_citizen(4)
    s.change_citizen_type(4)
    s.change_citizen_type(4, "Test District")
    assert old.get_superior() is None
    assert old.get_all_subordinates() == []


def test_change_citizen_type_old_c() -> None:
    """Test that this method removes the old citizen from the heirarchy"""
    s = sample_society1()
    old = s.get_citizen(7)
    c8 = Citizen(8, 'Citizen 8', 3001, 'Watcher', 10)
    s.add_citizen(c8, 7)
    s.change_citizen_type(7)
    assert old.get_superior() is None
    assert old.get_all_subordinates() == []


def test_change_citizen_type_head() -> None:
    """Test to make sure the society heirarchy is the same after head"""
    s = sample_society1()
    direct_subs = s.get_citizen(1).get_direct_subordinates()
    all_subs = s.get_citizen(1).get_all_subordinates()
    job = s.get_citizen(1).job
    rating = s.get_citizen(1).rating
    manufacturer = s.get_citizen(1).manufacturer
    year = s.get_citizen(1).model_year
    s.change_citizen_type(1)
    assert s.get_head() == s.get_citizen(1)
    assert s.get_citizen(1).get_direct_subordinates() == direct_subs
    assert s.get_citizen(1).get_all_subordinates() == all_subs
    assert s.get_citizen(1).job == job
    assert s.get_citizen(1).rating == rating
    assert s.get_citizen(1).manufacturer == manufacturer
    assert s.get_citizen(1).model_year == year
    assert s.get_citizen(1).get_superior() is None


###########################################################################
# Tests for method in Task 3.1
###########################################################################
def test_swap_up() -> None:
    """Test swap_up basic case"""
    s = sample_society1()
    under = s.get_citizen(6)
    under_job = under.job
    over = s.get_citizen(2)
    over_job = over.job
    under = s._swap_up(under)
    over = s.get_citizen(2)
    assert under.get_superior().cid == 1
    assert under.get_direct_subordinates() == [s.get_citizen(2),
                                               s.get_citizen(5)]
    assert over.get_superior() == under
    assert over.get_direct_subordinates() == [s.get_citizen(8),
                                              s.get_citizen(9),
                                              s.get_citizen(10)]
    assert isinstance(under, DistrictLeader)
    assert not isinstance(over, DistrictLeader)
    assert under.job == over_job
    assert over.job == under_job


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


def test_promote_citizen_head() -> None:
    """Tests that promote citizen does nothing if we try promoting the head"""
    s = sample_society1()
    head = s.get_head()
    subordinates = head.get_direct_subordinates()
    s.promote_citizen(head.cid)
    assert s.get_head() == head
    assert subordinates == head.get_direct_subordinates()


def test_promote_citizen_dl() -> None:
    """Tests that promote citizen does nothing if we try promoting a district leader"""
    s = sample_society1()
    who = s.get_citizen(7)
    superior = who.get_superior()
    direct = who.get_direct_subordinates()
    all = who.get_all_subordinates()
    s.promote_citizen(7)
    new = s.get_citizen(7)
    assert new.get_superior() == superior
    assert new.get_direct_subordinates() == direct
    assert new.get_all_subordinates() == all


def test_promote_citizen_lower() -> None:
    """Tests that promote citizen does nothing if we try promoting a subordinate with a lower rating"""
    s = sample_society1()
    who = s.get_citizen(4)
    superior = who.get_superior()
    direct = who.get_direct_subordinates()
    all = who.get_all_subordinates()
    s.promote_citizen(4)
    new = s.get_citizen(4)
    assert new.get_superior() == superior
    assert new.get_direct_subordinates() == direct
    assert new.get_all_subordinates() == all


def test_promote_citizen_new_head() -> None:
    """Test this method on making a new head"""
    s = sample_society1()
    who = s.get_citizen(3)
    superior = who.get_superior()
    all = s.get_head().get_all_subordinates().copy()
    all.remove(who)
    super_job = superior.job
    citizen_job = who.job
    superior = s.change_citizen_type(1, "Test District")
    s.promote_citizen(3)
    new = s.get_citizen(3)
    direct = [s.get_citizen(1), s.get_citizen(2), s.get_citizen(4)]
    all = merge(all, [s.get_citizen(1)])
    all2 = new.get_all_subordinates()
    assert new.get_superior() is None
    assert new.get_direct_subordinates() == direct
    assert all == all2
    assert s.get_citizen(1) in new.get_direct_subordinates()
    assert superior.job == citizen_job
    assert who.job == super_job
    assert isinstance(s.get_citizen(3), DistrictLeader)
    assert not isinstance(s.get_citizen(1), DistrictLeader)


def test_promote_citizen_multiple() -> None:
    """Test that promote_citizen can make multiple swaps"""
    s = sample_society1()
    s.change_citizen_type(2)
    s.get_citizen(9).rating = 100
    s.promote_citizen(9)
    assert s.get_head() == s.get_citizen(9)
    assert s.get_citizen(9).get_superior() is None
    assert s.get_citizen(9).job == "Big boss"
    assert s.get_citizen(6).get_superior() == s.get_citizen(2)
    assert s.get_citizen(6).job == "Farmer"
    assert s.get_citizen(2).get_superior() == s.get_citizen(1)
    assert s.get_citizen(2).job == "Coach"
    assert s.get_citizen(1).get_superior() == s.get_citizen(9)
    assert s.get_citizen(1).job == "Bank robber"


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


def test_delete_citizen_single() -> None:
    """Test that this society becomes empty after deleting the only head"""
    s = Society()
    c1 = Citizen(1, "Manufacturer", 3000, "Job", 90)
    s.add_citizen(c1)
    assert s.get_head() is c1
    s.delete_citizen(1)
    assert s.get_head() is None
    assert c1.get_superior() is None


def test_delete_citizen_head() -> None:
    """Test that the highest rated subordinate becomes the new head"""
    s = sample_society1()
    c11 = Citizen(11, "Manufacturer", 3000, "Job", 1)
    c12 = Citizen(12, "Manufacturer", 3000, "Job", 1)
    s.add_citizen(c11, 3)
    s.add_citizen(c12, 3)
    s.delete_citizen(1)
    assert s.get_head() == s.get_citizen(3)
    assert s.get_citizen(3).get_direct_subordinates() == [s.get_citizen(2),
                                                          s.get_citizen(4),
                                                          s.get_citizen(11),
                                                          s.get_citizen(12)]


if __name__ == '__main__':
    import pytest

    pytest.main(['a2_sample_test_paulo.py'])

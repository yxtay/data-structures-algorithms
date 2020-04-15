from src.list import OrderedList, UnorderedList


def test_unordered():
    my_list = UnorderedList()

    assert my_list.is_empty() == True

    my_list.add(31)
    assert my_list.is_empty() == False
    assert my_list.size() == 1

    my_list.add(77)
    my_list.add(17)
    my_list.add(93)
    my_list.add(26)
    my_list.add(54)

    assert my_list.is_empty() == False
    assert my_list.size() == 6
    assert my_list.search(17) == True

    my_list.remove(17)
    assert my_list.is_empty() == False
    assert my_list.size() == 5
    assert my_list.search(17) == False


def test_ordered():
    my_list = OrderedList()

    assert my_list.is_empty() == True

    my_list.add(31)
    assert my_list.is_empty() == False
    assert my_list.size() == 1

    my_list.add(77)
    my_list.add(17)
    my_list.add(93)
    my_list.add(26)
    my_list.add(54)

    assert my_list.is_empty() == False
    assert my_list.size() == 6
    assert my_list.search(17) == 0
    items = list(my_list)
    assert items == [17, 26, 31, 54, 77, 93]

    my_list.remove(17)
    assert my_list.is_empty() == False
    assert my_list.size() == 5
    assert my_list.search(17) == -1
    items = list(my_list)
    assert items == [26, 31, 54, 77, 93]

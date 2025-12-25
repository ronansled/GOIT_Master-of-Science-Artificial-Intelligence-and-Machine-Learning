from linked_list import SinglyLinkedList, merge_two_sorted_lists


def test_reverse():
    lst = SinglyLinkedList()
    for value in [1, 2, 3, 4, 5]:
        lst.append(value)

    lst.reverse()
    assert lst.to_list() == [5, 4, 3, 2, 1]
    print("Reverse test passed")


def test_sort():
    lst = SinglyLinkedList()
    for value in [4, 2, 5, 1, 3]:
        lst.append(value)

    lst.sort()
    assert lst.to_list() == [1, 2, 3, 4, 5]
    print("Sort test passed")


def test_merge():
    list1 = SinglyLinkedList()
    list2 = SinglyLinkedList()

    for v in [1, 3, 5]:
        list1.append(v)

    for v in [2, 4, 6]:
        list2.append(v)

    merged = merge_two_sorted_lists(list1, list2)
    assert merged.to_list() == [1, 2, 3, 4, 5, 6]
    print("Merge test passed")


def test_edge_cases():
    empty = SinglyLinkedList()
    empty.reverse()
    empty.sort()
    assert empty.to_list() == []

    single = SinglyLinkedList()
    single.append(10)
    single.reverse()
    single.sort()
    assert single.to_list() == [10]

    print("Edge cases test passed")


if __name__ == "__main__":
    test_reverse()
    test_sort()
    test_merge()
    test_edge_cases()
    print("All tests passed successfully")

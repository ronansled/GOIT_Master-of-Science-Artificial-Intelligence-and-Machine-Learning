from avl_tree import AVLTree


def test_find_min() -> None:
    tree = AVLTree()
    values = [10, 20, 5, 4, 15, 30, 25]

    for v in values:
        tree.insert(v)

    result = tree.find_min()
    expected = 4

    assert result == expected, f"Expected {expected}, got {result}"
    print("TEST PASSED: Minimum value =", result)


def test_single_element() -> None:
    tree = AVLTree()
    tree.insert(99)

    assert tree.find_min() == 99
    print("TEST PASSED: Single element tree")


def test_empty_tree() -> None:
    tree = AVLTree()
    try:
        tree.find_min()
    except ValueError:
        print("TEST PASSED: Empty tree raises ValueError")
    else:
        raise AssertionError("Expected ValueError for empty tree")


if __name__ == "__main__":
    test_find_min()
    test_single_element()
    test_empty_tree()

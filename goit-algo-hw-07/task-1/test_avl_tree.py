from avl_tree import AVLTree


def test_find_max() -> None:
    tree = AVLTree()
    values = [10, 20, 5, 4, 15, 30, 25]

    for v in values:
        tree.insert(v)

    result = tree.find_max()
    expected = 30

    assert result == expected, f"Expected {expected}, got {result}"
    print("TEST PASSED: Maximum value =", result)


def test_single_element() -> None:
    tree = AVLTree()
    tree.insert(42)

    assert tree.find_max() == 42
    print("TEST PASSED: Single element tree")


def test_empty_tree() -> None:
    tree = AVLTree()
    try:
        tree.find_max()
    except ValueError:
        print("TEST PASSED: Empty tree raises ValueError")
    else:
        raise AssertionError("Expected ValueError for empty tree")


if __name__ == "__main__":
    test_find_max()
    test_single_element()
    test_empty_tree()

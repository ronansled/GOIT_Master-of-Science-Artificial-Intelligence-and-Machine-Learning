from avl_tree import AVLTree


def test_sum_values() -> None:
    tree = AVLTree()
    values = [10, 20, 5, 4, 15, 30, 25]

    for v in values:
        tree.insert(v)

    result = tree.sum_values()
    expected = sum(values)

    assert result == expected, f"Expected {expected}, got {result}"
    print("TEST PASSED: Sum of values =", result)


def test_single_element() -> None:
    tree = AVLTree()
    tree.insert(7)

    assert tree.sum_values() == 7
    print("TEST PASSED: Single element tree")


def test_empty_tree() -> None:
    tree = AVLTree()

    result = tree.sum_values()
    assert result == 0
    print("TEST PASSED: Empty tree returns 0")


if __name__ == "__main__":
    test_sum_values()
    test_single_element()
    test_empty_tree()

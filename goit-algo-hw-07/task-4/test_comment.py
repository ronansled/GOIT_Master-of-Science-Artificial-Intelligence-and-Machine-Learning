from comment import Comment


def build_large_comment_tree() -> Comment:
    """
    Створює велике ієрархічне дерево коментарів
    з різною глибиною вкладеності.
    """
    root = Comment("Це найкращий роман року", "Олег")

    r1 = Comment("Не погоджуюсь", "Ірина")
    r2 = Comment("Поясніть чому", "Дмитро")
    r3 = Comment("Мені теж сподобалось", "Анна")

    root.add_reply(r1)
    root.add_reply(r2)
    root.add_reply(r3)

    r1_1 = Comment("Сюжет слабкий", "Максим")
    r1_2 = Comment("Персонажі картонні", "Олена")
    r1.add_reply(r1_1)
    r1.add_reply(r1_2)

    r1_1_1 = Comment("А мені зайшло", "Павло")
    r1_1.add_reply(r1_1_1)

    r2_1 = Comment("Бо стиль написання", "Катерина")
    r2.add_reply(r2_1)

    r2_1_1 = Comment("Так, автор молодець", "Юрій")
    r2_1.add_reply(r2_1_1)

    r3_1 = Comment("Особливо фінал", "Марія")
    r3.add_reply(r3_1)

    return root


def test_large_tree_display() -> None:
    root = build_large_comment_tree()

    print("\n=== COMMENT TREE ===")
    root.display()


def test_logical_deletion_preserves_children() -> None:
    root = build_large_comment_tree()

    comment_to_delete = root.replies[0]  # "Не погоджуюсь"
    comment_to_delete.remove_reply()

    print("\n=== AFTER LOGICAL DELETION ===")
    root.display()

    assert comment_to_delete.is_deleted is True
    assert len(comment_to_delete.replies) == 2


def test_deep_nested_deletion() -> None:
    root = build_large_comment_tree()

    deep_comment = root.replies[0].replies[0]  # "Сюжет слабкий"
    deep_comment.remove_reply()

    print("\n=== AFTER DEEP DELETION ===")
    root.display()

    assert deep_comment.is_deleted is True
    assert deep_comment.text == "Цей коментар було видалено."


def test_add_reply_after_deletion() -> None:
    root = build_large_comment_tree()

    deleted_comment = root.replies[1]  # "Поясніть чому"
    deleted_comment.remove_reply()

    new_reply = Comment("Навіть після видалення можна відповідати", "Тест")
    deleted_comment.add_reply(new_reply)

    print("\n=== ADD REPLY AFTER DELETION ===")
    root.display()

    assert len(deleted_comment.replies) == 2


def test_single_comment_tree() -> None:
    root = Comment("Один коментар", "Admin")

    print("\n=== SINGLE COMMENT ===")
    root.display()

    assert root.is_deleted is False
    assert root.replies == []


if __name__ == "__main__":
    test_large_tree_display()
    test_logical_deletion_preserves_children()
    test_deep_nested_deletion()
    test_add_reply_after_deletion()
    test_single_comment_tree()

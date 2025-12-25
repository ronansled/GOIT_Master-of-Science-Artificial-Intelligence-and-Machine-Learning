class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = Node(value)

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

    # 1. Реверсування списку
    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    # 2. Сортування злиттям
    def sort(self):
        self.head = self._merge_sort(self.head)

    def _merge_sort(self, head):
        if not head or not head.next:
            return head

        middle = self._get_middle(head)
        next_to_middle = middle.next
        middle.next = None

        left = self._merge_sort(head)
        right = self._merge_sort(next_to_middle)

        return self._sorted_merge(left, right)

    @staticmethod
    def _get_middle(head):
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    @staticmethod
    def _sorted_merge(left, right):
        if not left:
            return right
        if not right:
            return left

        if left.value <= right.value:
            left.next = SinglyLinkedList._sorted_merge(left.next, right)
            return left
        else:
            right.next = SinglyLinkedList._sorted_merge(left, right.next)
            return right


# 3. Об'єднання двох відсортованих списків
def merge_two_sorted_lists(list1, list2):
    dummy = Node(0)
    tail = dummy

    a = list1.head
    b = list2.head

    while a and b:
        if a.value <= b.value:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next

    tail.next = a if a else b

    result = SinglyLinkedList()
    result.head = dummy.next
    return result

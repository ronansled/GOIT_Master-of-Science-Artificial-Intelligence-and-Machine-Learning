from __future__ import annotations
from typing import Optional


class AVLNode:
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.left: Optional["AVLNode"] = None
        self.right: Optional["AVLNode"] = None
        self.height: int = 1


class AVLTree:
    def __init__(self) -> None:
        self.root: Optional[AVLNode] = None

    def insert(self, value: int) -> None:
        self.root = self._insert(self.root, value)

    def _insert(self, node: Optional[AVLNode], value: int) -> AVLNode:
        if node is None:
            return AVLNode(value)

        if value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)

        node.height = 1 + max(self._height(node.left), self._height(node.right))
        balance = self._balance_factor(node)

        if balance > 1 and value < node.left.value:
            return self._rotate_right(node)

        if balance < -1 and value > node.right.value:
            return self._rotate_left(node)

        if balance > 1 and value > node.left.value:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if balance < -1 and value < node.right.value:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def find_min(self) -> int:
        """
        Повертає найменше значення в AVL-дереві.
        Для BST/AVL мінімум завжди знаходиться
        у крайньому лівому вузлі.
        """
        if self.root is None:
            raise ValueError("Tree is empty")

        current = self.root
        while current.left is not None:
            current = current.left

        return current.value

    @staticmethod
    def _height(node: Optional[AVLNode]) -> int:
        return node.height if node else 0

    def _balance_factor(self, node: AVLNode) -> int:
        return self._height(node.left) - self._height(node.right)

    def _rotate_left(self, z: AVLNode) -> AVLNode:
        y = z.right
        t2 = y.left

        y.left = z
        z.right = t2

        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))

        return y

    def _rotate_right(self, z: AVLNode) -> AVLNode:
        y = z.left
        t3 = y.right

        y.right = z
        z.left = t3

        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))

        return y

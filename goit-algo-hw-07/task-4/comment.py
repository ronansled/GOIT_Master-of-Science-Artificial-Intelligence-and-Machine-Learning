from __future__ import annotations
from typing import List


class Comment:
    def __init__(self, text: str, author: str) -> None:
        self.text: str = text
        self.author: str = author
        self.replies: List["Comment"] = []
        self.is_deleted: bool = False

    def add_reply(self, reply: "Comment") -> None:
        self.replies.append(reply)

    def remove_reply(self) -> None:
        """
        Логічне видалення коментаря.
        Сам коментар зберігається в дереві,
        але його текст замінюється стандартним повідомленням.
        """
        self.text = "Цей коментар було видалено."
        self.is_deleted = True

    def display(self, level: int = 0) -> None:
        indent = " " * 4 * level

        if self.is_deleted:
            print(f"{indent}{self.text}")
        else:
            print(f"{indent}{self.author}: {self.text}")

        for reply in self.replies:
            reply.display(level + 1)

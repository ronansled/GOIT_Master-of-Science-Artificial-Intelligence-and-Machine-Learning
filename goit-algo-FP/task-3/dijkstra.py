import heapq
from typing import Dict, List, Tuple


class Graph:
    def __init__(self):
        self.adjacency: Dict[str, List[Tuple[str, int]]] = {}

    def add_edge(self, from_node: str, to_node: str, weight: int):
        """Додає ребро у обидва напрямки (неорієнтований граф)"""
        self.adjacency.setdefault(from_node, []).append((to_node, weight))
        self.adjacency.setdefault(to_node, []).append((from_node, weight))

    def dijkstra(self, start: str) -> Dict[str, float]:
        """Реалізація алгоритму Дейкстри"""
        distances = {node: float("inf") for node in self.adjacency}
        distances[start] = 0

        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            # Пропускаємо, якщо вже знайшли коротший шлях
            if current_distance > distances[current_node]:
                continue

            # Розглядаємо всіх сусідів
            for neighbor, weight in self.adjacency[current_node]:
                distance = current_distance + weight

                # Оновлюємо відстань, якщо знайшли коротший шлях
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

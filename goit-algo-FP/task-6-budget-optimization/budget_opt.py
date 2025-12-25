from typing import Dict, Tuple, List


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


def greedy_algorithm(items: Dict[str, Dict[str, int]], budget: int) -> Dict[str, int]:
    """
    Жадібний вибір за коефіцієнтом (calories / cost).
    Кожен товар можна вибрати не більше одного разу (0/1).
    Повертає словник {item_name: 1} для вибраних товарів.
    """
    # Список (item, ratio, cost, calories)
    ranked: List[Tuple[str, float, int, int]] = []
    for name, data in items.items():
        cost = data["cost"]
        calories = data["calories"]
        ratio = calories / cost if cost > 0 else float("inf")
        ranked.append((name, ratio, cost, calories))

    # Сортування за спаданням ratio
    ranked.sort(key=lambda x: x[1], reverse=True)

    chosen: Dict[str, int] = {}
    remaining = budget

    for name, _, cost, _ in ranked:
        if cost <= remaining:
            chosen[name] = 1
            remaining -= cost

    return chosen


def dynamic_programming(items: Dict[str, Dict[str, int]], budget: int) -> Dict[str, int]:
    """
    0/1 knapsack: максимізуємо сумарні calories при ліміті budget (cost).
    Повертає словник {item_name: 1} для вибраних товарів.
    """
    names = list(items.keys())
    n = len(names)
    # dp[i][w] — максимальні калорії, використовуючи перші i предметів і бюджет w
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name = names[i - 1]
        cost = items[name]["cost"]
        cal = items[name]["calories"]
        for w in range(budget + 1):
            # не брати
            not_take = dp[i - 1][w]
            take = -1
            if cost <= w:
                take = dp[i - 1][w - cost] + cal
            dp[i][w] = max(not_take, take)

    # Відтворення вибраних предметів
    w = budget
    chosen: Dict[str, int] = {}
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            name = names[i - 1]
            chosen[name] = 1
            w -= items[name]["cost"]

    return chosen


def summary(selection: Dict[str, int], items: Dict[str, Dict[str, int]]) -> Dict[str, int]:
    """
    Підрахунок загальної вартості та калорій для словника вибраних предметів.
    Повертає {'total_cost': ..., 'total_calories': ...}
    """
    total_cost = 0
    total_calories = 0
    for name, cnt in selection.items():
        if cnt:
            total_cost += items[name]["cost"] * cnt
            total_calories += items[name]["calories"] * cnt
    return {"total_cost": total_cost, "total_calories": total_calories}

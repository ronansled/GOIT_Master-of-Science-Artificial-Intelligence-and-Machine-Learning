import random
from collections import Counter
from typing import Dict, Tuple


def simulate_two_dice(n_rolls: int) -> Tuple[Counter, Dict[int, float]]:
    """
    Симуляція кидання двох чесних шестигранних кубиків.

    :param n_rolls: кількість кидків (має бути > 0)
    :return: (лічильник сум, словник ймовірностей сум 2..12)
    """
    if n_rolls <= 0:
        raise ValueError("n_rolls must be positive")

    sums = []
    for _ in range(n_rolls):
        roll_sum = random.randint(1, 6) + random.randint(1, 6)
        sums.append(roll_sum)

    counts = Counter(sums)
    probabilities = {s: counts.get(s, 0) / n_rolls for s in range(2, 13)}
    return counts, probabilities


def analytical_probabilities() -> Dict[int, float]:
    """
    Аналітичні ймовірності сум 2..12 при киданні двох чесних кубиків.
    """
    combinations = {
        2: 1,
        3: 2,
        4: 3,
        5: 4,
        6: 5,
        7: 6,
        8: 5,
        9: 4,
        10: 3,
        11: 2,
        12: 1,
    }
    total = 36
    return {s: c / total for s, c in combinations.items()}

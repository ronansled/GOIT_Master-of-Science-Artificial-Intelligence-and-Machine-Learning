from typing import Dict, List

COINS: List[int] = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(amount: int) -> Dict[int, int]:
    result: Dict[int, int] = {}

    for coin in COINS:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count

    return result


def find_min_coins(amount: int) -> Dict[int, int]:
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    last_coin = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in COINS:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                last_coin[i] = coin

    result: Dict[int, int] = {}
    while amount > 0:
        coin = last_coin[amount]
        result[coin] = result.get(coin, 0) + 1
        amount -= coin

    return result

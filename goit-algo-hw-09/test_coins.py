from coins import find_coins_greedy, find_min_coins


def test_small_amount() -> None:
    amount = 113

    greedy = find_coins_greedy(amount)
    dp = find_min_coins(amount)

    assert sum(k * v for k, v in greedy.items()) == amount
    assert sum(k * v for k, v in dp.items()) == amount

    print("113 GREEDY:", greedy)
    print("113 DP:", dp)


def test_large_amount() -> None:
    amount = 10_000

    greedy = find_coins_greedy(amount)
    dp = find_min_coins(amount)

    assert sum(k * v for k, v in greedy.items()) == amount
    assert sum(k * v for k, v in dp.items()) == amount

    print("10000 GREEDY coins:", sum(greedy.values()))
    print("10000 DP coins:", sum(dp.values()))


def test_edge_cases() -> None:
    assert find_coins_greedy(0) == {}
    assert find_min_coins(0) == {}

    assert find_coins_greedy(1) == {1: 1}
    assert find_min_coins(1) == {1: 1}

    print("EDGE CASES PASSED")


if __name__ == "__main__":
    test_small_amount()
    test_large_amount()
    test_edge_cases()
    print("ALL TESTS PASSED")

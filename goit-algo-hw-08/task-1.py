import heapq


def min_connection_cost(cables: list[int]) -> int:
    heapq.heapify(cables)
    total = 0

    while len(cables) > 1:
        a = heapq.heappop(cables)
        b = heapq.heappop(cables)
        cost = a + b
        total += cost
        heapq.heappush(cables, cost)

    return total


def test():
    assert min_connection_cost([4, 3, 2, 6]) == 29
    assert min_connection_cost([1, 2, 3, 4, 5]) == 33
    assert min_connection_cost([10]) == 0
    assert min_connection_cost([5, 5]) == 10
    print("ALL TESTS PASSED")


if __name__ == "__main__":
    test()

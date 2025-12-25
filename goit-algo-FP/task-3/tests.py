from dijkstra import Graph


def test_dijkstra_basic():
    graph = Graph()

    graph.add_edge("A", "B", 4)
    graph.add_edge("A", "C", 2)
    graph.add_edge("B", "C", 1)
    graph.add_edge("B", "D", 5)
    graph.add_edge("C", "D", 8)
    graph.add_edge("C", "E", 10)
    graph.add_edge("D", "E", 2)
    graph.add_edge("D", "F", 6)
    graph.add_edge("E", "F", 3)

    distances = graph.dijkstra("A")

    assert distances["A"] == 0
    assert distances["B"] == 3
    assert distances["C"] == 2
    assert distances["D"] == 8
    assert distances["E"] == 10
    assert distances["F"] == 13

    print("Basic Dijkstra test passed")


def test_single_node():
    graph = Graph()
    graph.add_edge("A", "A", 0)

    distances = graph.dijkstra("A")
    assert distances["A"] == 0

    print("Single node test passed")


def test_disconnected_graph():
    graph = Graph()
    graph.add_edge("A", "B", 1)
    graph.add_edge("C", "D", 2)

    distances = graph.dijkstra("A")

    assert distances["A"] == 0
    assert distances["B"] == 1
    assert distances["C"] == float("inf")
    assert distances["D"] == float("inf")

    print("Disconnected graph test passed")


if __name__ == "__main__":
    test_dijkstra_basic()
    test_single_node()
    test_disconnected_graph()
    print("All tests passed successfully")

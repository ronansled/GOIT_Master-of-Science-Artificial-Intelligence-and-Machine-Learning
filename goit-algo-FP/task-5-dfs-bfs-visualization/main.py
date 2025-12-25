import uuid
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="#1f1f1f"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)

        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)

        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)

    return graph


def draw_tree(root, title):
    tree = nx.DiGraph()
    pos = {root.id: (0, 0)}
    add_edges(tree, root, pos)

    colors = [data["color"] for _, data in tree.nodes(data=True)]
    labels = {node: data["label"] for node, data in tree.nodes(data=True)}

    plt.figure(figsize=(10, 6))
    plt.title(title)
    nx.draw(
        tree,
        pos=pos,
        labels=labels,
        arrows=False,
        node_size=2500,
        node_color=colors
    )
    plt.show()


def generate_color(step, total_steps):
    intensity = int(30 + (225 * step / total_steps))
    return f"#{intensity:02x}{intensity:02x}ff"


def bfs(root):
    queue = deque([root])
    visited = []

    while queue:
        node = queue.popleft()
        visited.append(node)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return visited


def dfs(root):
    stack = [root]
    visited = []

    while stack:
        node = stack.pop()
        visited.append(node)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return visited


def visualize_traversal(root, traversal_func, title):
    nodes = traversal_func(root)
    total = len(nodes)

    for i, node in enumerate(nodes):
        node.color = generate_color(i, total)

    draw_tree(root, title)


if __name__ == "__main__":
    # Створення дерева
    root = Node(0)
    root.left = Node(4)
    root.right = Node(1)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right.left = Node(3)
    root.right.right = Node(7)

    visualize_traversal(root, bfs, "BFS — обхід у ширину")
    visualize_traversal(root, dfs, "DFS — обхід у глибину")

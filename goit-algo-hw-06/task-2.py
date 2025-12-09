import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# ===== ГРАФ З ПЕРШОГО ЗАВДАННЯ =====
G = nx.Graph()
topics = [
    'Python_programming', 'NetworkX', 'Graph_theory', 'Wikipedia', 'Data_science',
    'Power_BI', 'Excel', 'Pandas', 'Machine_learning', 'Artificial_intelligence',
    'Ukraine', 'Kyiv', 'Lviv', 'Data_analysis', 'Business_intelligence'
]
G.add_nodes_from(topics)
edges = [
    ('Python_programming', 'NetworkX'), ('Python_programming', 'Pandas'),
    ('NetworkX', 'Graph_theory'), ('Graph_theory', 'Data_science'),
    ('Wikipedia', 'Data_science'), ('Wikipedia', 'Ukraine'),
    ('Data_science', 'Power_BI'), ('Data_science', 'Excel'),
    ('Data_science', 'Pandas'), ('Data_science', 'Machine_learning'),
    ('Machine_learning', 'Artificial_intelligence'),
    ('Power_BI', 'Business_intelligence'), ('Excel', 'Business_intelligence'),
    ('Pandas', 'Data_analysis'), ('Business_intelligence', 'Data_analysis'),
    ('Ukraine', 'Kyiv'), ('Ukraine', 'Lviv')
]
G.add_edges_from(edges)

# ===== РЕАЛІЗАЦІЯ DFS =====
def dfs_path(graph, start, goal, path=None):
    if path is None:
        path = []
    path = path + [start]
    
    if start == goal:
        return path
    
    for neighbor in graph.neighbors(start):
        if neighbor not in path:
            new_path = dfs_path(graph, neighbor, goal, path)
            if new_path:
                return new_path
    return None

# ===== РЕАЛІЗАЦІЯ BFS =====
def bfs_path(graph, start, goal):
    queue = deque([[start]])
    visited = set()
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        
        if node == goal:
            return path
        
        if node not in visited:
            visited.add(node)
            for neighbor in graph.neighbors(node):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    return None

# ===== ТЕСТОВІ ПАРИ ВЕРШИН =====
test_pairs = [
    ('Python_programming', 'Data_science'),
    ('Wikipedia', 'Business_intelligence'),
    ('Ukraine', 'Artificial_intelligence'),
    ('NetworkX', 'Kyiv')
]

print("=== ПОРІВНЯННЯ DFS та BFS ===")
print("="*60)

for start, goal in test_pairs:
    print(f"\nШлях від '{start}' до '{goal}':")
    
    # DFS
    dfs_result = dfs_path(G, start, goal)
    print(f"DFS: {'N/A' if dfs_result is None else ' → '.join(dfs_result)}")
    
    # BFS  
    bfs_result = bfs_path(G, start, goal)
    print(f"BFS: {'N/A' if bfs_result is None else ' → '.join(bfs_result)}")
    
    if dfs_result and bfs_result:
        print(f"  Довжина DFS: {len(dfs_result)-1}, BFS: {len(bfs_result)-1}")
    print("-" * 40)

# ===== ВІЗУАЛІЗАЦІЯ ПРИКЛАДУ =====
start, goal = 'Python_programming', 'Data_science'
dfs_path_result = dfs_path(G, start, goal)
bfs_path_result = bfs_path(G, start, goal)

plt.figure(figsize=(15, 5))

# Граф
pos = nx.spring_layout(G, k=3, iterations=50)
nx.draw(G, pos, with_labels=True, node_color='lightblue', 
        node_size=1500, font_size=8, alpha=0.7)

# DFS шлях (червоний)
if dfs_path_result:
    nx.draw_networkx_nodes(G, pos, nodelist=dfs_path_result, 
                          node_color='red', node_size=2000, alpha=0.9)
    nx.draw_networkx_edges(G, pos, edgelist=list(nx.utils.pairwise(dfs_path_result)),
                          edge_color='red', width=3)

# BFS шлях (зелений)  
if bfs_path_result:
    nx.draw_networkx_nodes(G, pos, nodelist=bfs_path_result, 
                          node_color='green', node_size=2000, alpha=0.9)
    nx.draw_networkx_edges(G, pos, edgelist=list(nx.utils.pairwise(bfs_path_result)),
                          edge_color='green', width=3)

plt.title(f"DFS (червоний) vs BFS (зелений): {start} → {goal}", fontsize=12)
plt.axis('off')
plt.tight_layout()
plt.show()

print(f"\nПриклад візуалізації: {start} → {goal}")
print(f"DFS шлях: {' → '.join(dfs_path_result) if dfs_path_result else 'N/A'}")
print(f"BFS шлях: {' → '.join(bfs_path_result) if bfs_path_result else 'N/A'}")

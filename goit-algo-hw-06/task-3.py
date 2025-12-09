import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations

# ===== ГРАФ З ПЕРШОГО ЗАВДАННЯ З ВАГАМИ =====
G = nx.Graph()

topics = [
    'Python_programming', 'NetworkX', 'Graph_theory', 'Wikipedia', 'Data_science',
    'Power_BI', 'Excel', 'Pandas', 'Machine_learning', 'Artificial_intelligence',
    'Ukraine', 'Kyiv', 'Lviv', 'Data_analysis', 'Business_intelligence'
]

G.add_nodes_from(topics)

# Ребра ЗІ ВАГАМИ (реалістичні відстані між темами Вікіпедії)
weighted_edges = [
    # Програмування та дані
    ('Python_programming', 'NetworkX', 2), ('Python_programming', 'Pandas', 1),
    ('NetworkX', 'Graph_theory', 1), ('Graph_theory', 'Data_science', 2),
    
    # Вікіпедія та дані
    ('Wikipedia', 'Data_science', 3), ('Wikipedia', 'Ukraine', 4),
    
    # Data_science - центральний хаб
    ('Data_science', 'Power_BI', 2), ('Data_science', 'Excel', 2),
    ('Data_science', 'Pandas', 1), ('Data_science', 'Machine_learning', 1),
    
    # ML ланцюжок
    ('Machine_learning', 'Artificial_intelligence', 1),
    
    # BI ланцюжок
    ('Power_BI', 'Business_intelligence', 1), ('Excel', 'Business_intelligence', 2),
    ('Pandas', 'Data_analysis', 1), ('Business_intelligence', 'Data_analysis', 1),
    
    # Україна
    ('Ukraine', 'Kyiv', 1), ('Ukraine', 'Lviv', 2)
]

for u, v, weight in weighted_edges:
    G.add_edge(u, v, weight=weight)

print("=== АЛГОРИТМ ДЕЙКСТРИ: НАЙКОРОТШІ ШЛЯХИ ===")
print(f"Граф: {len(G.nodes())} вершин, {len(G.edges())} зважених ребер\n")

# ===== РЕАЛІЗАЦІЯ ДЕЙКСТРИ =====
def dijkstra_path(graph, start, goal):
    """Знаходить найкоротший шлях від start до goal"""
    distances = {node: float('inf') for node in graph.nodes()}
    distances[start] = 0
    predecessors = {node: None for node in graph.nodes()}
    
    queue = [(0, start)]
    
    while queue:
        current_distance, current_node = min(queue, key=lambda x: x[0])
        
        if current_node == goal:
            # Реконструюємо шлях
            path = []
            total_weight = distances[current_node]
            while current_node is not None:
                path.append(current_node)
                current_node = predecessors[current_node]
            return path[::-1], total_weight
        
        queue = [(dist, node) for dist, node in queue if node != current_node]
        
        for neighbor in graph.neighbors(current_node):
            distance = graph[current_node][neighbor]['weight']
            new_distance = distances[current_node] + distance
            
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                predecessors[neighbor] = current_node
                queue.append((new_distance, neighbor))
    
    return None, float('inf')

# ===== ОБЧИСЛЕННЯ ВСІХ НАЙКОРОТШИХ ШЛЯХІВ =====
all_pairs = list(combinations(topics[:8], 2))  # Обмежуємо для демонстрації

print("НАЙКОРОТШІ ШЛЯХИ МІЖ ВЕРШИНАМИ:")
print("-" * 80)
results = []

for start, goal in all_pairs:
    path, distance = dijkstra_path(G, start, goal)
    if path:
        path_str = ' → '.join(path)
        print(f"{start:20} → {goal:20} | Шлях: {path_str} | Вага: {distance}")
        results.append((start, goal, path, distance))
    else:
        print(f"{start:20} → {goal:20} | Шлях: НЕ ЗНАЙДЕНО")
    print()

# ===== ВІЗУАЛІЗАЦІЯ =====
plt.figure(figsize=(14, 10))

pos = nx.spring_layout(G, k=4, iterations=100)

# Базовий граф
nx.draw_networkx_nodes(G, pos, node_size=2000, node_color='lightblue', alpha=0.7)
nx.draw_networkx_edges(G, pos, alpha=0.3, width=1)

# Найкоротші шляхи (товсті ребра)
for _, _, path, _ in results[:5]:  # Показуємо перші 5 шляхів
    path_edges = list(nx.utils.pairwise(path))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, 
                          edge_color='red', width=3, alpha=0.8, style='solid')

nx.draw_networkx_labels(G, pos, font_size=8, font_weight='bold')
plt.title("Алгоритм Дейкстри: найкоротші шляхи (червоні ребра)", fontsize=14)
plt.axis('off')
plt.tight_layout()
plt.show()

# ===== СТАТИСТИКА =====
print("\n=== СТАТИСТИКА ДЕЙКСТРИ ===")
min_path = min(results, key=lambda x: x[3])
max_path = max(results, key=lambda x: x[3])

print(f"Найкоротший шлях: {min_path[0]} → {min_path[1]} ({min_path[3]})")
print(f"{' → '.join(min_path[2])}")
print(f"Найдовший шлях: {max_path[0]} → {max_path[1]} ({max_path[3]})")
print(f"{' → '.join(max_path[2])}")

# Перевірка NetworkX вбудованим алгоритмом
print("\nПеревірка NetworkX shortest_path_length:")
for start, goal in [('Python_programming', 'Data_science'), 
                   ('Wikipedia', 'Artificial_intelligence')]:
    nx_dist = nx.shortest_path_length(G, start, goal, weight='weight')
    nx_path = nx.shortest_path(G, start, goal, weight='weight')
    print(f"{start} → {goal}: {nx_dist}, {' → '.join(nx_path)} ✓")

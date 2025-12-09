import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Створюємо граф Вікіпедії (модель зв'язків статей)
G = nx.Graph()

# Вершини - теми статей
topics = [
    'Python_programming', 'NetworkX', 'Graph_theory', 'Wikipedia', 'Data_science',
    'Power_BI', 'Excel', 'Pandas', 'Machine_learning', 'Artificial_intelligence',
    'Ukraine', 'Kyiv', 'Lviv', 'Data_analysis', 'Business_intelligence'
]

G.add_nodes_from(topics)

# Ребра - гіперпосилання між статтями
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

# ===== АНАЛІЗ ГРАФУ =====
print("=== АНАЛІЗ ГРАФУ ВІКІПЕДІЇ ===")
print(f"Кількість вершин: {G.number_of_nodes()}")
print(f"Кількість ребер: {G.number_of_edges()}")
print(f"Щільність графа: {nx.density(G):.3f}")

degrees = dict(G.degree())
avg_degree = sum(degrees.values()) / len(degrees)
print(f"Середній ступінь: {avg_degree:.2f}")
print(f"Вершина з max ступенем: {max(degrees, key=degrees.get)} ({max(degrees.values())})\n")

# ТОП-3 центральності
degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)

print("ТОП-3 за ступенем:")
for node, cent in sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)[:3]:
    print(f"  {node}: {cent:.3f}")

print("\nТОП-3 за міжвершинною центральністю:")
for node, cent in sorted(betweenness_centrality.items(), key=lambda x: x[1], reverse=True)[:3]:
    print(f"  {node}: {cent:.4f}\n")

# ===== ВІЗУАЛІЗАЦІЯ =====
plt.figure(figsize=(12, 8))

# Позиції вершин
pos = nx.spring_layout(G, k=3, iterations=50)

# Розмір вузлів пропорційний ступеню
node_sizes = [degrees[node] * 400 for node in G.nodes()]
node_colors = [degrees[node] for node in G.nodes()]

# Малюємо граф
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, 
                      cmap=plt.cm.Reds, alpha=0.9)
nx.draw_networkx_edges(G, pos, alpha=0.5, width=1.5)
nx.draw_networkx_labels(G, pos, font_size=8, font_weight='bold')

plt.title("Модель мережі Вікіпедії (розмір = ступінь вершини)", fontsize=14, pad=20)
plt.axis('off')
plt.tight_layout()
plt.show()

# ===== СТАТИСТИКА У ТАБЛИЦІ =====
print("\nСтупені всіх вершин:")
print("Вершина".ljust(25), "Ступінь")
print("-" * 35)
for node in sorted(degrees, key=degrees.get, reverse=True):
    print(f"{node[:22]:<25} {degrees[node]}")

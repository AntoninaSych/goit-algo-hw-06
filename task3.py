import networkx as nx
import matplotlib.pyplot as plt
import csv
from collections import deque
import heapq

def read_csv(filename):
    data = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

def build_graph(stations_data, connections_data, max_nodes=None, max_edges=None):
    G = nx.Graph()
    added_nodes = 0
    added_edges = 0

    for station in stations_data:
        if max_nodes is not None and added_nodes >= max_nodes:
            break
        G.add_node(station['name'], latitude=float(station['latitude']), longitude=float(station['longitude']))
        added_nodes += 1

    for connection in connections_data:
        if max_edges is not None and added_edges >= max_edges:
            break
        station1 = connection['station1']
        station2 = connection['station2']
        station1_name = next((station['name'] for station in stations_data if station['id'] == station1), None)
        station2_name = next((station['name'] for station in stations_data if station['id'] == station2), None)
        if station1_name is not None and station2_name is not None:
            weight = float(connection['time'])  # Додамо час як вагу ребра
            G.add_edge(station1_name, station2_name, weight=weight)
            added_edges += 1

    return G

def visualize_graph(G):
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_size=500, font_size=8, font_weight='normal')
    plt.title("London Underground Station Network")
    plt.show()

def analyze_graph(G):
    print("Number of nodes:", G.number_of_nodes())
    print("Number of edges:", G.number_of_edges())

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next_vertex in set(graph[vertex]) - set(path):
            if next_vertex == goal:
                yield path + [next_vertex]
            else:
                stack.append((next_vertex, path + [next_vertex]))

def bfs_paths(graph, start, goal):
    queue = deque([(start, [start])])
    while queue:
        (vertex, path) = queue.popleft()
        for next_vertex in set(graph[vertex]) - set(path):
            if next_vertex == goal:
                yield path + [next_vertex]
            else:
                queue.append((next_vertex, path + [next_vertex]))

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph.nodes()}  # Ініціалізуємо всі відстані як нескінченні
    distances[start] = 0
    visited = set()

    priority_queue = [(0, start)]

    while priority_queue:
        (current_distance, current_node) = heapq.heappop(priority_queue)

        if current_node not in visited:
            visited.add(current_node)

            for neighbor, weight in graph[current_node].items():
                distance = current_distance + weight['weight']
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

    return distances

def visualize_paths(G, paths, start, end):
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_size=500, font_size=8, font_weight='normal')

    for i, path in enumerate(paths, start=1):
        nx.draw_networkx_edges(G, pos, edgelist=[(path[j], path[j+1]) for j in range(len(path)-1)], 
                               edge_color='r', width=2, label=f"Path {i}")

    plt.title(f"London Underground Station Network with Paths from {start} to {end}")
    plt.legend()
    plt.show()

stations_data = read_csv('london.stations.csv')
connections_data = read_csv('london.connections.csv')

max_nodes = 50  # Максимальна кількість вершин (None - без обмежень)
max_edges = 100  # Максимальна кількість ребер (None - без обмежень)

G = build_graph(stations_data, connections_data, max_nodes, max_edges)
analyze_graph(G)
visualize_graph(G)

# Визначимо початкову та кінцеву станції
start_station = 'Acton Town'
end_station = 'Aldgate East'

# Знайдемо та візуалізуємо шляхи для DFS та BFS
dfs_result = list(dfs_paths(G, start_station, end_station))
bfs_result = list(bfs_paths(G, start_station, end_station))

print("DFS шляхи між {} та {}: {}".format(start_station, end_station, dfs_result))
print("BFS шляхи між {} та {}: {}".format(start_station, end_station, bfs_result))

visualize_paths(G, dfs_result, start_station, end_station)
visualize_paths(G, bfs_result, start_station, end_station)

# Знайдемо найкоротші шляхи використовуючи алгоритм Дейкстри
shortest_paths = {station: dijkstra(G, station) for station in G.nodes()}
print("Найкоротші шляхи від станції {} до всіх інших станцій:".format(start_station))
for station, distances in shortest_paths.items():
    print(f"{station}: {distances}")


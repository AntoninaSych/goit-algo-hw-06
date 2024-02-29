import networkx as nx
import matplotlib.pyplot as plt
import csv

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
            G.add_edge(station1_name, station2_name)
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

stations_data = read_csv('london.stations.csv')
connections_data = read_csv('london.connections.csv')

max_nodes = 10  # Максимальна кількість вершин (None - без обмежень)
max_edges = None  # Максимальна кількість ребер (None - без обмежень)

G = build_graph(stations_data, connections_data, max_nodes, max_edges)
visualize_graph(G)
analyze_graph(G)

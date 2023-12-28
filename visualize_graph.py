import networkx as nx
import matplotlib.pyplot as plt

def plot_graph(graph, pos, path=None, title="Graph"):
    plt.figure(figsize=(8, 8))
    nx.draw(graph, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=8, font_color='black', font_weight='bold', font_family='sans-serif')
    
    if path:
        edges = list(zip(path[:-1], path[1:]))
        nx.draw_networkx_edges(graph, pos, edgelist=edges, edge_color='red', width=2)

    plt.title(title)
    plt.show()

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = find_all_paths(graph, node, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths

# Given coordinates
# coordinates = {
#     0: (0, 0),
#     1: (0, 100),
#     2: (100, 100),
#     3: (100, 30),
#     4: (50, 50),
#     5: (70, 70),
#     6: (10, 10)
# }
# 0 0 100 100 30 50 70 10
coordinates = {
    (0,0): {
        (30,50): {
            
        }
    }
}

# Create a graph
G = nx.Graph()

# Add nodes with coordinates
for node, coord in coordinates.items():
    G.add_node(node, pos=coord)

# Add edges
edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 0)]
G.add_edges_from(edges)

# Get node positions
pos = nx.get_node_attributes(G, 'pos')

# Find all paths from (0, 0) to (100, 100)
start_node = 0
end_node = 2  # Node corresponding to (100, 100)
all_paths = find_all_paths(G, start_node, end_node)

# Visualize all paths
for path in all_paths:
    plot_graph(G, pos, path, f"Path: {path}")

# Visualize the entire graph
plot_graph(G, pos, title="Graph")

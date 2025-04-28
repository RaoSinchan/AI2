import heapq

def dijkstra(graph, source):
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    priority_queue = [(0, source)]
    visited = set()

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue
        visited.add(current_node)

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# --- User Input Part ---

graph = {}

n = int(input("Enter number of nodes: "))
for _ in range(n):
    node = input("Enter node name: ")
    graph[node] = []

e = int(input("Enter number of edges: "))
print("Enter edges in format: start_node end_node weight")
for _ in range(e):
    u, v, w = input().split()
    w = int(w)
    graph[u].append((v, w))
    graph[v].append((u, w))  # because the graph is undirected

source_node = input("Enter source node: ")

# Run Dijkstra
shortest_paths = dijkstra(graph, source_node)

# Output shortest paths
print(f"\nShortest path costs from source node '{source_node}':")
for node, cost in shortest_paths.items():
    print(f"{source_node} -> {node} = {cost}")


''' Enter number of nodes: 5
Enter node name: A
Enter node name: B
Enter node name: C
Enter node name: D
Enter node name: E
Enter number of edges: 6
Enter edges in format: start_node end_node weight
A B 2
A C 4
B C 1
B D 7
C E 3
D E 2
Enter source node: A
'''

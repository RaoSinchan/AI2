import heapq
def prims_algorithm(n, edges):
    graph = {i: [] for i in range(n)}
    for u, v, weight in edges:
        graph[u].append((v, weight))
        graph[v].append((u, weight))  # Undirected graph

    visited = [False] * n
    min_heap = [(0, 0, -1)]  # (weight, current_vertex, parent_vertex)
    mst = []
    total_cost = 0

    while min_heap:
        weight, u, parent = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        if parent != -1:
            mst.append((parent, u, weight))
            total_cost += weight
        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v, u))
    
    return mst, total_cost

# --- Taking Input from User ---
n = int(input("Enter the number of vertices: "))
e = int(input("Enter the number of edges: "))

edges = []
print("Enter each edge as: u v weight (space separated)")
for _ in range(e):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

# Execute Prim's Algorithm
mst_edges, cost = prims_algorithm(n, edges)

# Output
print("\nList of edges in the Minimum Spanning Tree:")
for u, v, w in mst_edges:
    print(f"(u,v, weight) = ({u},{v},{w})")
    print(f"\nTotal cost of the spanning tree = {cost}")


'''
Enter the number of vertices: 4
Enter the number of edges: 5
Enter each edge as: u v weight (space separated)
0 1 10
0 2 6
0 3 5
1 3 15
2 3 4
'''

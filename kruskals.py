class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        u_root = self.find(u)
        v_root = self.find(v)
        if u_root == v_root:
            return False
        # Union by rank
        if self.rank[u_root] < self.rank[v_root]:
            self.parent[u_root] = v_root
        elif self.rank[u_root] > self.rank[v_root]:
            self.parent[v_root] = u_root
        else:
            self.parent[v_root] = u_root
            self.rank[u_root] += 1
        return True

def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])  # Sort edges based on weight
    ds = DisjointSet(n)
    mst = []
    total_weight = 0
    for u, v, weight in edges:
        if ds.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight
    return mst, total_weight

# --- Taking Input from User ---
n = int(input("Enter the number of vertices: "))
e = int(input("Enter the number of edges: "))

edges = []
print("Enter each edge as: u v weight (space separated):")
for _ in range(e):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

# Run Kruskal's algorithm
mst_result, total_cost = kruskal(n, edges)

# Output
print("\nEdges in the Minimum Spanning Tree:")
for u, v, w in mst_result:
    print(f"(u,v, weight) = ({u},{v},{w})")

print(f"\nTotal cost of the spanning tree = {total_cost}")

'''
Enter the number of vertices: 4
Enter the number of edges: 5
Enter each edge as: u v weight (space separated):
0 1 10
0 2 6
0 3 5
1 3 15
2 3 4
'''

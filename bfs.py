# Function to perform BFS
def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# Main Program
graph = {}

# Taking user input for the graph
n = int(input("Enter the number of nodes: "))
for _ in range(n):
    node = input("Enter node name: ")
    edges = input(f"Enter the neighbors of {node} separated by space: ").split()
    graph[node] = edges

visited = []  # List to keep track of visited nodes
queue = []    # Initialize a queue

start_node = input("Enter the starting node for BFS: ")

print("\nBFS Traversal:")
bfs(visited, graph, start_node)

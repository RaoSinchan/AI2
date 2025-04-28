# Function to perform DFS
def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Main Program
graph = {}

# Taking user input for the graph
n = int(input("Enter the number of nodes: "))
for _ in range(n):
    node = input("Enter node name: ")
    edges = input(f"Enter the neighbors of {node} separated by space: ").split()
    graph[node] = edges

visited = set()  # Set to keep track of visited nodes

start_node = input("Enter the starting node for DFS: ")

print("\nFollowing is the Path using Depth-First Search:")
dfs(visited, graph, start_node)




'''
Enter the number of nodes: 6
Enter node name: A
Enter the neighbors of A separated by space: B C
Enter node name: B
Enter the neighbors of B separated by space: D E
Enter node name: C
Enter the neighbors of C separated by space: F
Enter node name: D
Enter the neighbors of D separated by space:
Enter node name: E
Enter the neighbors of E separated by space: F
Enter node name: F
Enter the neighbors of F separated by space:

Enter the starting node for DFS: A

Following is the Path using Depth-First Search:
A
B
D
E
F
C
'''

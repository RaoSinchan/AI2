class GraphColoring:
    def __init__(self, graph, max_colors):
        self.graph = graph  
        self.num_vertices = len(graph)
        self.max_colors = max_colors
        self.colors = [-1] * self.num_vertices 

    def is_safe(self, vertex, color):
        for neighbor in range(self.num_vertices):
            if self.graph[vertex][neighbor] == 1 and self.colors[neighbor] == color:
                return False
        return True

    def branch_and_bound(self, vertex=0):
        if vertex == self.num_vertices:
            return True
        
        for color in range(1, self.max_colors + 1):
            if self.is_safe(vertex, color):
                self.colors[vertex] = color
                if self.branch_and_bound(vertex + 1):
                    return True
                self.colors[vertex] = -1  # backtrack
        
        return False
    
    def solve(self):
        if not self.branch_and_bound():
            print("Solution does not exist")
        else:
            print("Solution found:", self.colors)


# ------------------ User Input Section ------------------

# Take number of vertices
n = int(input("Enter the number of vertices: "))

# Take adjacency matrix input
print("Enter the adjacency matrix row by row (space-separated 0s and 1s):")
graph = []
for i in range(n):
    row = list(map(int, input(f"Enter row {i + 1}: ").split()))
    if len(row) != n:
        print("Row must have exactly", n, "elements!")
        exit()
    graph.append(row)

# Take number of colors
max_colors = int(input("Enter the maximum number of colors: "))

# Create a GraphColoring object and solve
graph_coloring = GraphColoring(graph, max_colors)
graph_coloring.solve()




'''
Enter the number of vertices: 4
Enter the adjacency matrix row by row (space-separated 0s and 1s):
Enter row 1: 0 1 1 0
Enter row 2: 1 0 1 0
Enter row 3: 1 1 0 1
Enter row 4: 0 0 1 0
Enter the maximum number of colors: 3

Solution found: [1, 2, 3, 1]

'''

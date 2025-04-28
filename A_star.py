class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    def h(self, n):
        # Heuristic values
        H = {}
        for node in self.adjacency_list.keys():
            H[node] = int(input(f"Enter heuristic value for node {node}: "))
        return H[n]

    def a_star_algorithm(self, start_node, stop_node):
        open_list = set([start_node])
        closed_list = set([])
        g = {}
        g[start_node] = 0
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            for v in open_list:
                if n is None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v

            if n is None:
                print('Path does not exist!')
                return None

            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)
                reconst_path.reverse()

                print('Path found: {}'.format(reconst_path))
                return reconst_path

            for (m, weight) in self.get_neighbors(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n
                        if m in closed_list:
                            closed_list.remove(m)
                        open_list.add(m)

            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None

# --- Main Program to take user input ---

adjacency_list = {}

n = int(input("Enter the number of nodes: "))
for _ in range(n):
    node = input("Enter node name: ")
    neighbors = []
    num_neighbors = int(input(f"Enter the number of neighbors for {node}: "))
    for _ in range(num_neighbors):
        neighbor, weight = input(f"Enter neighbor and weight (format: neighbor weight) for {node}: ").split()
        neighbors.append((neighbor, int(weight)))
    adjacency_list[node] = neighbors

graph1 = Graph(adjacency_list)

start_node = input("Enter the start node: ")
stop_node = input("Enter the stop (goal) node: ")

graph1.a_star_algorithm(start_node, stop_node)







'''
Enter the number of nodes: 3
Enter node name: A
Enter the number of neighbors for A: 3
Enter neighbor and weight (format: neighbor weight) for A: B 1
Enter neighbor and weight (format: neighbor weight) for A: C 3
Enter neighbor and weight (format: neighbor weight) for A: D 7
Enter node name: B
Enter the number of neighbors for B: 1
Enter neighbor and weight (format: neighbor weight) for B: D 5
Enter node name: C
Enter the number of neighbors for C: 1
Enter neighbor and weight (format: neighbor weight) for C: D 12

Enter heuristic value for node A: 1
Enter heuristic value for node B: 1
Enter heuristic value for node C: 1

Enter the start node: A
Enter the stop (goal) node: D
'''

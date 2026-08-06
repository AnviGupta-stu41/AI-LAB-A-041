def bfs(graph, start_node):
    visited = []
    queue = [start_node]

    while queue:
        current_node = queue.pop(0)

        if current_node not in visited:
            print(f"Exploring Node: {current_node}")
            visited.append(current_node)

            for neighbour in graph.get(current_node, []):
                if neighbour not in visited and neighbour not in queue:
                    queue.append(neighbour)

    return visited


print("----Build Your Graph----")

student_graph = {}

num_edges = int(input("How many edges does graph have? : "))

print("Enter the edges in the format u v")

for i in range(num_edges):
    u, v = input(f"Edge {i+1}: ").split()

    if u not in student_graph:
        student_graph[u] = []

    if v not in student_graph:
        student_graph[v] = []

    student_graph[u].append(v)
    student_graph[v].append(u)

start = input("Enter the starting node of BFS: ")

print("\nGraph Dictionary:", student_graph)
print("\nStarting BFS Traversal:")

visited = bfs(student_graph, start)

print(visited)
import heapq

def get_user_inputs():
    # 1. Take input for heuristic values
    heuristic = {}
    num_nodes = int(input("Enter total number of nodes: "))

    print("\nEnter heuristic value h(n) for each node:")
    for _ in range(num_nodes):
        node = input("Node name: ").strip().upper()
        h_val = float(input(f"Heuristic h({node}): "))
        heuristic[node] = h_val

    # 2. Take input for graph edges
    graph = {node: [] for node in heuristic}
    num_edges = int(input("\nEnter total number of directed edges: "))

    print("\nEnter edges in format (from_node to_node weight):")
    for i in range(num_edges):
        u, v, w = input(f"Edge {i + 1}: ").strip().split()
        u, v = u.upper(), v.upper()
        weight = float(w)
        
        if u not in graph:
            graph[u] = []
        graph[u].append((v, weight))

    return heuristic, graph


def astar(graph, heuristic, start, goal):
    # Priority Queue stores tuples of: (f_score, g_score, current_node)
    open_set = [(heuristic[start], 0, start)]
    came_from = {}
    g_cost = {node: float('inf') for node in heuristic}
    g_cost[start] = 0
    visited = set()

    while open_set:
        _, current_g, current_node = heapq.heappop(open_set)

        if current_node in visited:
            continue
        visited.add(current_node)

        # GOAL check & path reconstruction
        if current_node == goal:
            path = [current_node]
            while current_node in came_from:
                current_node = came_from[current_node]
                path.append(current_node)
            path.reverse()
            return path, g_cost[goal]

        # Neighbor exploration
        for neighbor, cost in graph.get(current_node, []):
            new_cost = current_g + cost

            if new_cost < g_cost.get(neighbor, float('inf')):
                g_cost[neighbor] = new_cost
                came_from[neighbor] = current_node
                f_score = new_cost + heuristic.get(neighbor, 0)
                heapq.heappush(open_set, (f_score, new_cost, neighbor))

    return None, float('inf')


# ------- Main Program --------------

if __name__ == "__main__":
    print("=== A* ALGORITHM INPUT SETUP ===\n")
    heuristic, graph = get_user_inputs()

    print("\n--- Path Finding ---")
    start = input("Enter start node: ").strip().upper()
    goal = input("Enter goal node: ").strip().upper()

    path, cost = astar(graph, heuristic, start, goal)

    print("\n=== RESULT ===")
    if path:
        print("Shortest path:", " -> ".join(path))
        print("Total path cost:", cost)
    else:
        print("Path not found.")
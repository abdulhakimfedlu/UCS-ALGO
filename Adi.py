import heapq

def uniform_cost_search(graph, start, goal):
    if start not in graph or goal not in graph:
        return None, float('inf')
    
    if start == goal:
        return [start], 0
    
    open_set = [(0, start, [start])]
    g_score = {start: 0}
    
    while open_set:
        current_g, current, path = heapq.heappop(open_set)
        
        if current == goal:
            return path, current_g
        
        for neighbor, edge_cost in graph.get(current, {}).items():
            tentative_g = current_g + edge_cost
            
            if tentative_g < g_score.get(neighbor, float('inf')):
                g_score[neighbor] = tentative_g
                new_path = path + [neighbor]
                heapq.heappush(open_set, (tentative_g, neighbor, new_path))
    
    return None, float('inf')



toy_graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'D': 1, 'E': 5},
    'C': {'D': 3},
    'D': {'E': 2},
    'E': {'F': 6},
    'F':{}
}

print("\n--- UNIFORM COST SEARCH TESTER ---")
print("Available nodes:", list(toy_graph.keys()))
print("-----------------------------------\n")

# Take user input
start = input("Enter the START node: ").strip().upper()
goal = input("Enter the GOAL node: ").strip().upper()

# Run the search
path, cost = uniform_cost_search(toy_graph, start, goal)

# Show results
print("\n--- RESULT ---")
if path is None:
    print("No path found. Maybe the nodes are not connected or spelled wrong.")
else:
    print("Cheapest Path:", " -> ".join(path))
    print("Total Cost:", cost)

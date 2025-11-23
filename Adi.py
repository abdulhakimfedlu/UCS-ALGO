import heapq

def uniform_cost_search(graph, start, goal):
    """
    Uniform Cost Search: Finds lowest-cost path from start to goal.
    
    :param graph: Dict {node: {neighbor: cost}}
    :param start, goal: Nodes
    :return: (path list, total_cost) or None if no path
    """
    if start not in graph or goal not in graph:
        return None, float('inf')
    
    if start == goal:
        return [start], 0
    
    open_set = [(0, start, [start])]  # (g, node, path)
    came_from = {start: None}
    g_score = {start: 0}
    
    while open_set:
        current_g, current, path = heapq.heappop(open_set)
        
        if current == goal:
            return path, current_g
        
        for neighbor, edge_cost in graph.get(current, {}).items():
            tentative_g = current_g + edge_cost
            
            if tentative_g < g_score.get(neighbor, float('inf')):
                g_score[neighbor] = tentative_g
                came_from[neighbor] = current
                new_path = path + [neighbor]
                heapq.heappush(open_set, (tentative_g, neighbor, new_path))
    
    return None, float('inf')
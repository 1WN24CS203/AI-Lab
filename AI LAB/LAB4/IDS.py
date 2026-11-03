def depth_limited_search(node, goal, graph, limit, path):
    if node == goal:
        return path
    
    if limit == 0:
        return "cutoff"
    
    cutoff_occurred = False
    
    for child in graph.get(node, []):
        if child not in path:
            # Fixed: Properly append the unique child to the tracking path matrix
            result = depth_limited_search(
                child, goal, graph, limit - 1, path + [child]
            )
            
            if isinstance(result, list):
                return result
            
            if result == "cutoff":
                cutoff_occurred = True
                
    if cutoff_occurred:
        return "cutoff"
    else:
        return "failure"


def iterative_deepening_search(initial, goal, graph, maximum_depth):
    for depth in range(maximum_depth + 1):
        result = depth_limited_search(initial, goal, graph, depth, path=[initial])
        
        if isinstance(result, list):
            return result
            
    return "failure"


if __name__ == "__main__":
    print("Input:")
    initial_state = input("Initial State: ").strip()
    goal_state = input("Goal State: ").strip()
    maximum_depth = int(input("Maximum Depth: ").strip())
    print("\nSearch Tree:")
    
    nodes = [initial_state]
    if goal_state not in nodes:
        nodes.append(goal_state)
        
    graph = {}
    i = 0
    
    while i < len(nodes):
        node = nodes[i]
        adjacent_input = input(f"{node}: ").strip()
        
        if adjacent_input == "-" or not adjacent_input:
            graph[node] = []
        else:
            neighbors = [n.strip() for n in adjacent_input.split() if n.strip()]
            graph[node] = neighbors
            
            for neighbor in neighbors:
                if neighbor not in nodes:
                    nodes.append(neighbor)
        i += 1

    path_result = iterative_deepening_search(initial_state, goal_state, graph, maximum_depth)
    
    print("\nOutput:")
    if isinstance(path_result, list):
        print(" -> ".join(path_result))
    else:
        print(path_result)

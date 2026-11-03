import heapq

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0) # 0 represents the blank space

class Node:
    def __init__(self, state, parent=None, action=None, g=0, h=0):
        self.state = state      # Tuple of length 9
        self.parent = parent
        self.action = action
        self.g = g              # Path cost
        self.h = h              # Heuristic cost
        self.f = g + h          # Total cost

    def __lt__(self, other):
        return self.f < other.f

def manhattan_distance(state):
    dist = 0
    for i, tile in enumerate(state):
        if tile != 0:
            # Current coordinates (row, col)
            r1, c1 = i // 3, i % 3
            # Goal coordinates (row, col)
            goal_idx = GOAL.index(tile)
            r2, c2 = goal_idx // 3, goal_idx % 3
            dist += abs(r1 - r2) + abs(c1 - c2)
    return dist

def child_node(state, action):
    lst = list(state)
    blank = lst.index(0)
    r, c = blank // 3, blank % 3
    
    # Calculate target indices based on movement boundaries
    if action == 'UP' and r > 0: target = blank - 3
    elif action == 'DOWN' and r < 2: target = blank + 3
    elif action == 'LEFT' and c > 0: target = blank - 1
    elif action == 'RIGHT' and c < 2: target = blank + 1
    else: return None # Invalid boundary move
    
    lst[blank], lst[target] = lst[target], lst[blank]
    return tuple(lst)

def a_star(start_state):
    root = Node(start_state, h=manhattan_distance(start_state))
    frontier = [root]
    explored = set()
    
    while frontier:
        node = heapq.heappop(frontier)
        
        if node.state == GOAL:
            path = []
            while node.parent:
                path.append((node.action, node.state))
                node = node.parent
            return path[::-1] # Reverse tracking to show forward path
            
        if node.state not in explored:
            explored.add(node.state)
            
            for action in ['UP', 'DOWN', 'LEFT', 'RIGHT']:
                next_state = child_node(node.state, action)
                if next_state and next_state not in explored:
                    g_cost = node.g + 1
                    h_cost = manhattan_distance(next_state)
                    child = Node(next_state, node, action, g_cost, h_cost)
                    heapq.heappush(frontier, child)
    return None

# --- Verification & Simulation Run ---
if __name__ == "__main__":
    # 0 is the empty tile. Easy configuration solving in a few moves
    start = (1, 2, 3, 4, 0, 6, 7, 5, 8) 
    
    print("Initial State Grid:")
    print(f"{start[0:3]}\n{start[3:6]}\n{start[6:9]}\n")
    
    solution = a_star(start)
    if solution:
        print(f"Goal Reached in {len(solution)} moves!")
        for step, (act, st) in enumerate(solution, 1):
            print(f"Step {step} -> Slide {act}:")
            print(f"{st[0:3]}\n{st[3:6]}\n{st[6:9]}\n")
    else:
        print("No solution found.")

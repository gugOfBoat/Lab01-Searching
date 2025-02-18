import heapq

# 1.6. Graph-search A* (AStar)
def astar(arr, source, destination, heuristic):
    """
    A* algorithm:
    Parameters:
    ---------------------------
    arr: list / numpy array 
        The graph's adjacency matrix
    source: integer
        Starting node
    destination: integer
        Ending node
    heuristic: list / numpy array
        The heuristic value from the current node to the goal
    
    Returns
    ---------------------
    visited: dictionary
        The dictionary contains visited nodes, each key is a visited node,
        each value is the adjacent node visited before it.
    path: list
        Founded path
    """
    # TODO

    path = []
    visited = {}
    
    frontier = [] #A priorityQueue
    
    heapq.heappush(frontier, (0 + heuristic[source], 0, source, None)) # fn, gn, node, parent

    while frontier:
        _, cost, current, parent = heapq.heappop(frontier)

        if current in visited and visited[current][1] <= cost:
            continue # IF we already have optimal path
            
        visited[current] = (parent, cost)

        if current == destination:
            break

        for neighbor in range(len(arr[current])):
            if arr[current][neighbor] > 0: #path valid
                newCost = cost + arr[current][neighbor] #gn = g(current) + path cost    
                f_n = newCost + heuristic[neighbor] # fn = gn + heuristic

                heapq.heappush(frontier, (f_n, newCost, neighbor, current)) #push new node to heap

    # for tracing
    if destination in visited:
        node = destination
        while node is not None:
            path.append(node)
            node = visited[node][0] # Back to parent
    path.reverse()
    return visited, path
import heapq

# 1.5. Greedy best first search (GBFS)
def gbfs(arr, source, destination, heuristic):
    """
    GBFS algorithm:
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
    frontier = [] # A priority queue

    heapq.heappush(frontier, (heuristic[source], source, None))

    while frontier:
        _, current, parent = heapq.heappop(frontier)

        if current in visited:
            continue

        visited[current] = parent

        if current == destination: # The goal reached
            break

        for neighbor in range(len(arr[current])):
            if arr[current][neighbor] > 0 and neighbor not in visited:
                heapq.heappush(frontier, (heuristic[neighbor], neighbor, current))
    
    # for tracing
    if destination in visited:
        node = destination
        while node is not None:
            path.append(node)
            node = visited[node] #Back to parent
        path.reverse()

    return visited, path
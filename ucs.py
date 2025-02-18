import heapq

# 1.3. Uniform-cost search (UCS)
def ucs(arr, source, destination):
    """
    UCS algorithm:
    Parameters:
    ---------------------------
    arr: list / numpy array 
        The graph's adjacency matrix
    source: integer
        Starting node
    destination: integer
        Ending node
    
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
    frontier = [] #A priority queue

    heapq.heappush(frontier, (0, source, None))

    while frontier:
        cost, current, parent = heapq.heappop(frontier)

        if current in visited: # Find optimal path before
            continue
        
        visited[current] = (parent, cost)

        if current == destination: # Reach the goal
            break
        
        for neighbor in range(len(arr[current])):
            if arr[current][neighbor] > 0 and neighbor not in visited:
                newCost = cost + arr[current][neighbor] # Update path cost
                heapq.heappush(frontier, (newCost, neighbor, current))

    # For tracing
    if destination in visited:
        node = destination
        while node is not None:
            path.append(node)
            node = visited[node][0] # Continue tracing
        path.reverse()

    return visited, path

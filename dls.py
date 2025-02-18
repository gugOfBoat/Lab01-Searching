
# 1.4.a. Depth-limited search
def dls(arr, source, destination, depth_limit):
    """
    DLS algorithm:
    Parameters:
    ---------------------------
    arr: list / numpy array 
        The graph's adjacency matrix
    source: integer
        Starting node
    destination: integer
        Ending node
    depth_limit: integer
        Maximum depth for search
    
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

    #Init
    frontier = [(source, 0)]
    visited[source] = None

    while frontier:
        current, depth = frontier.pop()

        if current == destination:
            break
        
        if depth < depth_limit:
            for neighbor in reversed(range(len(arr[current]))):
                if arr[current][neighbor] > 0 and neighbor not in visited:
                    # For tracing
                    visited[neighbor] = current
                    frontier.append((neighbor, depth + 1))

    # Make full path if goal expanded
    if destination in visited:
        node = destination
        while node is not None:
            path.append(node)
            node = visited[node]
        path.reverse()
    return visited, path

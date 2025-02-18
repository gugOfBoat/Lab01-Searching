# 1.2. Depth-first search (DFS)
def dfs(arr, source, destination):
    """
    DFS algorithm:
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

    #Init
    frontier = [source]
    visited[source] = None

    while frontier:
        current = frontier.pop()

        if current == destination:
            break
        
        for neighbor in reversed(range(len(arr[current]))):
            if arr[current][neighbor] != 0 and neighbor not in visited:
                # For tracing
                visited[neighbor] = current
                frontier.append(neighbor)

    # Make full path if goal expanded
    if destination in visited:
        node = destination
        while node is not None:
            path.append(node)
            node = visited[node]
        path.reverse()
        

    return visited, path
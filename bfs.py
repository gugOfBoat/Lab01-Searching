from collections import deque


# 1.1. Breadth-first search (BFS)
def bfs(arr, source, destination):
    """
    BFS algorithm:
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
    frontier = deque([source])
    visited[source] = None

    while frontier:
        current = frontier.popleft()


        if current == destination:
            break
        
        for neighbor, is_connected in enumerate(arr[current]):
            #If not have path and not visited
            if is_connected and neighbor not in visited: 
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


import random

def hc(arr, source, destination, heuristic):
    """
    First-Choice Hill Climbing (HC) Algorithm.

    Parameters:
    ---------------------------
    arr: list / numpy array 
        The graph's adjacency matrix
    source: int
        Starting node
    destination: int
        Ending node
    heuristic: list / numpy array
        The heuristic value from the current node to the goal
    
    Returns:
    ---------------------
    visited: dict
        A dictionary of visited nodes where each key is a visited node,
        and each value is the parent node visited before it.
    path: list
        The found path from source to destination.
    """

    path = []
    visited = {}
    current = source

    while current != destination:
        # Get the list of neighbors that haven't been visited yet
        neighbors = [i for i in range(len(arr[current])) if arr[current][i] > 0 and i not in visited]

        if not neighbors:
            break  # No more neighbors to visit, stop

        # Filter neighbors with a better (lower) heuristic value than the current node
        better_neighbors = [n for n in neighbors if heuristic[n] < heuristic[current]]

        if not better_neighbors:
            break  # No better neighbor found, stop

        # Randomly choose one of the better neighbors
        next_node = random.choice(better_neighbors)
        visited[next_node] = current  # Save the parent node for path tracing
        current = next_node  # Move to the next node

    # Trace back the path if the destination was reached
    if current == destination:
        node = destination
        while node is not None:
            path.append(node)
            node = visited.get(node)
        path.reverse()  # Reverse the path since it was built from destination to source

    return visited, path

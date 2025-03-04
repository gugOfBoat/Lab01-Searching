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
        # Get the list of neighbors
        neighbors = [i for i in range(len(arr[current])) if arr[current][i] > 0]

        if not neighbors:
            break  # No more neighbors to visit, stop

        random.shuffle(neighbors)  # Shuffle neighbors randomly to mimic First-Choice behavior

        for next_node in neighbors:
            if heuristic[next_node] < heuristic[current]:  # Select the first better neighbor found
                visited[next_node] = current  # Save the parent node for path tracing
                current = next_node  # Move to the next node
                break
        else:
            break  # No better neighbor found, stop

    # Trace back the path if the destination was reached
    if current == destination:
        node = destination
        while node is not None:
            path.append(node)
            node = visited.get(node)
        path.reverse()  # Reverse the path since it was built from destination to source

    return visited, path

from dls import dls
def ids(arr, source, destination, max_depth = None):
    """
    Iterative Deepening Search (IDS) - Depth-first search with increasing depth limits.

    Parameters:
    ---------------------------
    arr: list (2D array) - Adjacency matrix representing the graph
    source: int - Starting node
    destination: int - Goal node

    Returns:
    ---------------------
    visited: dict - Dictionary storing visited nodes `{node: parent}`
    path: list - Shortest path from `source` to `destination`
    """
    for depth_limit in range(len(arr)):  # Increase depth limit from 0 to N
        visited, path = dls(arr, source, destination, depth_limit)  # Call DLS

        if path:  # If DLS found a valid path, return the result
            return visited, path

    return {}, []  # If no path is found after trying all depths
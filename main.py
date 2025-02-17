# TODO: Import libraries
import time
import tracemalloc
from collections import deque

# 1. Search Strategies Implementation
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

    return visited, path


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

    return visited, path


# 1.4. Iterative deepening search (IDS)
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

    return visited, path


# 1.4.b. IDS
def ids(arr, source, destination):
    """
    IDS algorithm:
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

    return visited, path


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

    return visited, path


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

    return visited, path


# 1.7. Hill-climbing First-choice (HC)
def hc(arr, source, destination, heuristic):
    """
    HC algorithm:
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

    return visited, path

def readInputFile(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    numOfNodes = int(lines[0].strip())     # Read number of node in first line

    start, goal = map(int, lines[1].strip().split())     # Read start and goal

    adjacencyMatrix = []     # Read matrix
    for i in range(2, 2 + numOfNodes):
        row = list(map(int, lines[i].strip().split()))
        adjacencyMatrix.append(row)

    heuristic = list(map(int, lines[-1].strip().split())) if len(lines) > 2 + numOfNodes else None     # Read Heuristic(if any)

    return numOfNodes, start, goal, adjacencyMatrix, heuristic



# 2. Main function
if __name__ == "__main__":
    # TODO: Read the input data
    inputFile = "input.txt"
    numOfNodes, start, goal, adjacencyMatrix, heuristic = readInputFile(inputFile)

    # Print test
    print("Number of nodes:", numOfNodes)
    print("Start node:", start)
    print("Goal node:", goal)
    print("Adjacency Matrix:")

    for row in adjacencyMatrix:
        print(row)
    if heuristic:
        print("Heuristic values:", heuristic)

    # TODO: Start measuring

    tracemalloc.start()       # start supervise memory
    start_time = time.time()  # start supervise time complexity
    
    # TODO: Call a function to execute the path finding process

    path = []  # Init mt path

    visited, path = bfs(adjacencyMatrix, start, goal) # Call the bfs 

    # TODO: Stop measuring 

    end_time = time.time()      # Save the end time

    current, peak = tracemalloc.get_traced_memory()      # Get memory data

    tracemalloc.stop()       # Stop supervise memory

    # TODO: Show the output data
    output_file = "output.txt"

    with open(output_file, "w") as file:
        file.write("BFS:\n")

        # the Path
        if path:
            file.write("Path: " + " -> ".join(map(str, path)) + "\n")
        else:
            file.write("Path: -1\n")

        file.write(f"Time: {end_time - start_time:.7f} seconds\n")         # Excute time

        file.write(f"Memory: {peak / 1024:.2f} KB\n")         # Memory used

    print("✅ Output saved to", output_file)

    pass
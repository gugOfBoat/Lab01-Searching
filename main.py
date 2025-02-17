# TODO: Import libraries
import time
import heapq
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
    priorityQueue = []

    heapq.heappush(priorityQueue, (0, source, None))

    while priorityQueue:
        cost, current, parent = heapq.heappop(priorityQueue)

        if current in visited: # Find optimal path before
            continue
        
        visited[current] = (parent, cost)

        if current == destination: # Reach the goal
            break
        
        for neighbor in range(len(arr[current])):
            if arr[current][neighbor] > 0 and neighbor not in visited:
                newCost = cost + arr[current][neighbor] # Update path cost
                heapq.heappush(priorityQueue, (newCost, neighbor, current))

    # For tracing
    if destination in visited:
        node = destination
        while node is not None:
            path.append(node)
            node = visited[node][0] # Continue tracing
        path.reverse()

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


# 1.4.b. IDS
def ids(arr, source, destination):
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
    priorityQueue = []

    heapq.heappush(priorityQueue, (heuristic[source], source, None))

    while priorityQueue:
        _, current, parent = heapq.heappop(priorityQueue)

        if current in visited:
            continue

        visited[current] = parent

        if current == destination: # The goal reached
            break

        for neighbor in range(len(arr[current])):
            if arr[current][neighbor] > 0 and neighbor not in visited:
                heapq.heappush(priorityQueue, (heuristic[neighbor], neighbor, current))
        
    if destination in visited:
        node = destination
        while node is not None:
            path.append(node)
            node = visited[node]
        path.reverse()

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

# Function to measure time and memory for each search algorithm
def measure_memory(func, *args):
    tracemalloc.start()  # Start measuring memory
    start_time = time.perf_counter()  # Start measuring time
    visited, path = func(*args)  # Run the algorithm
    end_time = time.perf_counter()  # Stop measuring time
    current, peak = tracemalloc.get_traced_memory()  # Get memory usage
    tracemalloc.stop()  # Stop measuring memory

    return {
        "path": path,
        "time": end_time - start_time,
        "memory": peak / 1024  # Convert bytes to KB
    }

# Function to format results
def format_results(name, results):
    return (
        f"{name}:\n"
        f"Path: {' -> '.join(map(str, results['path'])) if results['path'] else '-1'}\n"
        f"Time: {results['time']:.7f} seconds\n"
        f"Memory: {results['memory']:.2f} KB\n\n"
    )


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

    bfs_results = measure_memory(bfs, adjacencyMatrix, start, goal)
    dfs_results = measure_memory(dfs, adjacencyMatrix, start, goal)
    ucs_results = measure_memory(ucs, adjacencyMatrix, start, goal)
    dls_results = measure_memory(dls, adjacencyMatrix, start, goal, 10)
    ids_results = measure_memory(ids, adjacencyMatrix, start, goal)
    gbfs_results = measure_memory(gbfs, adjacencyMatrix, start, goal, heuristic)
    # TODO: Stop measuring 

    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # TODO: Show the output data
    output_file = "output.txt"
    with open(output_file, "w") as file:
        file.write(format_results("BFS", bfs_results))
        file.write(format_results("DFS", dfs_results))
        file.write(format_results("UCS", ucs_results))
        file.write(format_results("DLS", dls_results))
        file.write(format_results("IDS", ids_results))
        file.write(format_results("GBFS", gbfs_results))
        
    print("✅ Output saved to", output_file)

    pass
import tracemalloc
import time

def measure_memory(func, *args):
    tracemalloc.start()
    start_time = time.perf_counter()
    visited, path = func(*args)
    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return {
        "path": path,
        "time": end_time - start_time,
        "memory": peak / 1024
    }

def format_results(name, results):
    return (
        f"{name}:\n"
        f"Path: {' -> '.join(map(str, results['path'])) if results['path'] else '-1'}\n"
        f"Time: {results['time']:.7f} seconds\n"
        f"Memory: {results['memory']:.2f} KB\n\n"
    )

def read_input_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    num_of_nodes = int(lines[0].strip())
    start, goal = map(int, lines[1].strip().split())

    adjacency_matrix = []
    for i in range(2, 2 + num_of_nodes):
        row = list(map(int, lines[i].strip().split()))
        adjacency_matrix.append(row)

    heuristic = list(map(int, lines[-1].strip().split())) if len(lines) > 2 + num_of_nodes else None
    return num_of_nodes, start, goal, adjacency_matrix, heuristic

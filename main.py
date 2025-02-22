from utils import measure_memory, format_results, read_input_file
from bfs import bfs
from dfs import dfs
from ucs import ucs
from dls import dls
from ids import ids
from gbfs import gbfs
from astar import astar
from hc import hc

# Read input data
input_file = "input.txt"
num_of_nodes, start, goal, adjacency_matrix, heuristic = read_input_file(input_file)

# Measure performance for all algorithms
bfs_results = measure_memory(bfs, adjacency_matrix, start, goal)
dfs_results = measure_memory(dfs, adjacency_matrix, start, goal)
ucs_results = measure_memory(ucs, adjacency_matrix, start, goal)
dls_results = measure_memory(dls, adjacency_matrix, start, goal, 10)  # Using depth limit 10
ids_results = measure_memory(ids, adjacency_matrix, start, goal)
gbfs_results = measure_memory(gbfs, adjacency_matrix, start, goal, heuristic)
astar_results = measure_memory(astar, adjacency_matrix, start, goal, heuristic)
hc_results = measure_memory(hc, adjacency_matrix, start, goal, heuristic)

# Save results to file
output_file = "output.txt"
with open(output_file, "w") as file:
    file.write(format_results("BFS", bfs_results))
    file.write(format_results("DFS", dfs_results))
    file.write(format_results("UCS", ucs_results))
    file.write(format_results("DLS", dls_results))
    file.write(format_results("IDS", ids_results))
    file.write(format_results("GBFS", gbfs_results))
    file.write(format_results("A*", astar_results))
    file.write(format_results("Hill climbing", hc_results))

print("✅ Output saved to", output_file)

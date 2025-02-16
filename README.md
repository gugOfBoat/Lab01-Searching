# Lab 1 - Searching (CSC14003)

This repository contains implementations of various graph search algorithms for **Lab 1 - Searching** in the **Introduction to Artificial Intelligence (CSC14003)** course.

## 📌 Project Description
The goal of this project is to implement and compare various search algorithms on a given graph. The program reads an input file, performs a path search from the start node to the goal node, and outputs the results, including the path, runtime, and memory usage.

## 🔍 Implemented Search Algorithms
- **Breadth-first search (BFS)**
- **Depth-first search (DFS)**
- **Uniform-cost search (UCS)**
- **Iterative deepening search (IDS)**
- **Greedy best-first search (GBFS)**
- **A* search (A\*)**
- **Hill-climbing (HC) variant**

## 📂 Project Structure
Lab01-Searching/ │── src/ # Source code of search algorithms │ ├── bfs.py # BFS algorithm │ ├── dfs.py # DFS algorithm │ ├── ucs.py # UCS algorithm │ ├── ids.py # IDS algorithm │ ├── gbfs.py # GBFS algorithm │ ├── astar.py # A* algorithm │ ├── hill_climbing.py # Hill Climbing algorithm │ ├── utils.py # Helper functions (file reading, etc.) │ ├── main.py # Main execution file │ │── test/ # Sample test cases │ ├── test1.txt │ ├── test2.txt │ │── docs/ # Documentation and report │ ├── report.pdf │ │── README.md # Project description and usage │── .gitignore # Ignore unnecessary files │── requirements.txt # Required Python libraries

markdown
Copy
Edit

## 📥 Input Format
The input file contains:
- **First line**: Number of nodes in the graph.
- **Second line**: Start node and goal node.
- **Subsequent lines**: Adjacency matrix of the graph.
- **Last line**: Heuristic values for each node (for heuristic-based algorithms).


## 📤 Output Format
- **Path found** from start to goal.
- **Execution time** and **memory usage**.

### 🔹 Example Output:
BFS: Path: 0 -> 1 -> 3 -> 4 Time: 0.0000003 seconds Memory: 8 KB

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Button, RadioButtons
from utils import read_input_file
from bfs import bfs
from dfs import dfs
from ucs import ucs
from gbfs import gbfs
from astar import astar
from hc import hc
from dls import dls
from ids import ids
import random

# Đọc dữ liệu từ input.txt
num_nodes, start, goal, adjacency_matrix, heuristic = read_input_file("input.txt")

# Danh sách thuật toán
algorithms = {
    "BFS": bfs,
    "DFS": dfs,
    "UCS": ucs,
    "GBFS": gbfs,
    "A*": astar,
    "First choice HC": hc,
    "DLS": dls,
    "IDS": ids
}

selected_algorithm = "BFS"
depth_limit = 10  # Độ sâu giới hạn cho DLS

def run_algorithm(event):
    """Hàm chạy thuật toán khi nhấn Start"""
    global visited_nodes, path, final_path, current_step
    algorithm_func = algorithms[selected_algorithm]

    if selected_algorithm in ["GBFS", "A*", "First choice HC"]:
        visited_nodes, path = algorithm_func(adjacency_matrix, start, goal, heuristic)
    elif selected_algorithm == "DLS":
        visited_nodes, path = algorithm_func(adjacency_matrix, start, goal, depth_limit)
    elif selected_algorithm == "IDS":
        visited_nodes, path = algorithm_func(adjacency_matrix, start, goal, max_depth=10)
    else:
        visited_nodes, path = algorithm_func(adjacency_matrix, start, goal)

    visited_nodes = list(visited_nodes.keys()) if isinstance(visited_nodes, dict) else visited_nodes
    final_path = path
    current_step = 0
    update_graph(0)

def update_graph(frame):
    """Hàm cập nhật đồ thị"""
    ax.clear()
    ax.set_axis_off()

    # Vẽ đồ thị gốc
    edge_labels = {(i, j): adjacency_matrix[i][j] for i, j in G.edges}
    nx.draw(G, pos, with_labels=True, labels={i: str(i) for i in range(num_nodes)},
            node_color='lightgray', edge_color='gray', node_size=800, font_size=10, ax=ax)
    
    # Hiển thị trọng số cạnh
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='black', font_size=8, label_pos=0.3, ax=ax)

    # Hiển thị heuristic ngay bên trên các node
    heuristic_labels = {i: f"h={heuristic[i]}" for i in range(len(heuristic))}
    heuristic_pos = {k: (v[0], v[1] + 0.08) for k, v in pos.items()}  # Dịch vị trí heuristic lên một chút
    nx.draw_networkx_labels(G, heuristic_pos, labels=heuristic_labels, font_size=8, font_color='blue', ax=ax)

    # Hiển thị nhãn "Start" và "Goal"
    special_labels = {start: "Start", goal: "Goal"}
    special_pos = {k: (v[0] + 0.1, v[1] + 0.1) for k, v in pos.items()}
    nx.draw_networkx_labels(G, special_pos, labels=special_labels, font_size=10, font_color='red', ax=ax)

    # Highlight các node đã duyệt (màu cam)
    if visited_nodes and frame < len(visited_nodes):
        nx.draw_networkx_nodes(G, pos, nodelist=visited_nodes[:frame+1], node_color='orange', ax=ax)

    # Highlight đường đi cuối cùng (màu đỏ)
    if frame >= len(visited_nodes) and final_path:
        nx.draw_networkx_nodes(G, pos, nodelist=final_path, node_color='red', ax=ax)
        edges_in_path = [(final_path[i], final_path[i+1]) for i in range(len(final_path) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=edges_in_path, edge_color='red', width=2, arrows=True, arrowstyle='-|>', ax=ax)

    ax.set_aspect('equal')
    ax.autoscale_view()
    fig.canvas.draw_idle()

def next_step(event):
    """Hàm thực hiện bước tiếp theo"""
    global current_step
    if current_step < len(visited_nodes):
        current_step += 1
        update_graph(current_step)

def select_algorithm(label):
    """Hàm chọn thuật toán từ Radio Button"""
    global selected_algorithm
    selected_algorithm = label

# Khởi tạo đồ thị
G = nx.Graph()
for i in range(num_nodes):
    for j in range(i + 1, num_nodes):
        try:
            if adjacency_matrix[i][j] > 0 and i != j:
                G.add_edge(i, j, weight=adjacency_matrix[i][j])
        except IndexError:
            print(f"❌ Lỗi: Truy cập adjacency_matrix[{i}][{j}] nhưng ma trận chỉ có {len(adjacency_matrix[i])} cột!")

# Cải thiện layout để tránh chồng lấn node
pos = nx.spring_layout(G, seed=42, k=10, iterations=300)  # Tăng giá trị k để giãn khoảng cách giữa các node

# Khởi tạo biến lưu trạng thái
visited_nodes, path = [], []
final_path = []
current_step = 0

# Tạo giao diện
fig, ax = plt.subplots(figsize=(18, 12))
ax.set_axis_off()
plt.subplots_adjust(left=0.25, right=0.98, bottom=0.2, top=0.98)

# Nút Start
ax_start = plt.axes([0.7, 0.02, 0.1, 0.05], frameon=False)
btn_start = Button(ax_start, "Start")
btn_start.on_clicked(run_algorithm)

# Nút Next Step
ax_next = plt.axes([0.82, 0.02, 0.12, 0.05], frameon=False)
btn_next = Button(ax_next, "Next Step")
btn_next.on_clicked(next_step)

# Radio chọn thuật toán
ax_algo = plt.axes([0.02, 0.5, 0.2, 0.35], frameon=False)
radio_algo = RadioButtons(ax_algo, list(algorithms.keys()))
radio_algo.on_clicked(select_algorithm)

plt.title("Graph Search Algorithm Visualization ")
plt.show()

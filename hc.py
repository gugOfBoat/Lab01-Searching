import random
import math

def hc(arr, source, destination, heuristic, T=1000, cooling_rate=0.95):
    """
    Hill Climbing Algorithm with Simulated Annealing (HC-SA)

    Parameters:
    ---------------------------
    arr: list (2D array) - Ma trận kề của đồ thị
    source: int - Nút bắt đầu
    destination: int - Nút kết thúc
    heuristic: list - Giá trị heuristic của từng nút
    T: float - Nhiệt độ ban đầu (quyết định khả năng đi xuống)
    cooling_rate: float - Hệ số giảm nhiệt độ

    Returns:
    ---------------------
    visited: dictionary - Danh sách các nút đã duyệt `{node: parent}`
    path: list - Đường đi từ `source` đến `destination`
    """
    path = []
    visited = {}
    current = source
    current_T = T  # Nhiệt độ ban đầu

    while current != destination and current_T > 1e-3:  # Dừng nếu nhiệt độ quá thấp
        neighbors = [i for i in range(len(arr[current])) if arr[current][i] > 0 and i not in visited]

        if not neighbors:
            break  # Không còn hàng xóm, dừng lại

        # Chọn hàng xóm có heuristic tốt nhất
        best_neighbor = min(neighbors, key=lambda x: heuristic[x])
        delta_E = heuristic[current] - heuristic[best_neighbor]  # Sự thay đổi heuristic

        # Nếu trạng thái mới tốt hơn, chấp nhận ngay
        if delta_E > 0:
            visited[best_neighbor] = current
            current = best_neighbor
        else:
            # Nếu trạng thái mới tệ hơn, chấp nhận với xác suất e^(delta_E / T)
            probability = math.exp(delta_E / current_T)
            if random.random() < probability:
                visited[best_neighbor] = current
                current = best_neighbor

        # Giảm nhiệt độ
        current_T *= cooling_rate

    # Truy vết đường đi nếu đến đích
    if current == destination:
        node = destination
        while node is not None:
            path.append(node)
            node = visited.get(node)
        path.reverse()

    return visited, path

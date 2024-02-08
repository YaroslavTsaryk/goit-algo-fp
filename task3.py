import heapq


def dijkstra(graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())
    heapq.heapify(unvisited)

    while unvisited:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        # Видаляємо поточну вершину з множини невідвіданих
        current_vertex = heapq.heappop(unvisited)

        # Якщо поточна відстань є нескінченністю, то ми завершили роботу
        if distances[current_vertex] == float("infinity"):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance

    return distances


# Приклад графа у вигляді словника
graph = {
    "A": {"B": 5, "C": 10},
    "B": {"A": 5, "D": 3},
    "C": {"A": 10, "D": 2},
    "D": {"B": 3, "C": 2, "E": 4},
    "E": {"D": 4},
}

# Виклик функції для вершини A
print(dijkstra(graph, "A"))
# {'A': 0, 'B': 5, 'C': 10, 'D': 8, 'E': 12}

import heapq

def dijkstra(graph, start):
    # Init all distances as infinity
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Skip if have shorter path
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            # If shorter path found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Test graph
graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 5), ('D', 10)],
    'C': [('A', 2), ('B', 5), ('D', 3)],
    'D': [('B', 10), ('C', 3), ('E', 1)],
    'E': [('D', 1)]
}

# define shortest paths from A:
start_vertex = 'A'
shortest_paths = dijkstra(graph, start_vertex)

print(f"Shortest paths from {start_vertex}:")
for vertex, distance in shortest_paths.items():
    print(f"{start_vertex} → {vertex}: {distance}")

# shortest paths from A:
# A → A: 0
# A → B: 4
# A → C: 2
# A → D: 5
# A → E: 6
import heapq

def dijkstra(graph, start, end):
    # Initialisation des distances et du tas
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    previous_nodes = {node: None for node in graph}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Si on atteint le sommet de destination
        if current_node == end:
            break

        # Si on trouve une distance plus longue que celle déjà enregistrée, on passe
        if current_distance > distances[current_node]:
            continue

        # Parcourir les voisins
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Si une distance plus courte est trouvée
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    # Reconstruction du chemin le plus court
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous_nodes[current]
    path.reverse()

    return path, distances[end]

# Exemple d'utilisation
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
end_node = 'D'
shortest_path, shortest_distance = dijkstra(graph, start_node, end_node)
print(f"Le plus court chemin de {start_node} à {end_node} est : {shortest_path} avec une distance de {shortest_distance}")

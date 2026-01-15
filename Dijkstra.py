graph = {
    'A': {'B': 1, 'C': 2, 'G': 1},
    'B': {'A': 1, 'D': 4, 'E': 5},
    'C': {'A': 2, 'E': 3, 'D': 2},
    'D': {'B': 4, 'C': 2, 'F': 1},
    'E': {'B': 5, 'C': 3, 'F': 3},
    'F': {'D': 1, 'E': 3, 'F': 1},
    'G': {'A': 1, 'H': 1},
    'H': {'F': 1, 'G': 1},
}


def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    prev = {node: None for node in graph}
    visited = {node: 0 for node in graph}

    dist[start] = 0
    unvisited = set(graph.keys())

    step = 0

    while unvisited:
        # 1. pick unvisited node with smallest current distance
        current = min(unvisited, key=lambda node: dist[node])
        if dist[current] == float('inf'):
            break

        print(f"\nStep {step}:")
        print(f"  Current node : {current}")
        print(f"  Distances    : {dist}")
        print(f"  Visited flags: {visited}")
        print(f"  Unvisited    : {unvisited}")
        step += 1

        visited[current] = 1

        # 2. relax all edges from current
        # 2. relax all edges from current
        for neighbor, weight in graph[current].items():
            if visited[neighbor]:
                continue

            new_dist = dist[current] + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                prev[neighbor] = current

        # 3. done with current
        unvisited.discard(current)

    return dist, prev, visited


def build_path(prev, start, end):
    path = []
    node = end
    while node is not None:
        path.append(node)
        node = prev[node]
    path.reverse()
    if not path or path[0] != start:
        return None
    return path


def print_table(dist, prev, visited):
    print("\nFinal table:")
    print("Node | Vis | Dist | Prev")
    print("-------------------------")
    for node in sorted(dist.keys()):
        vis = visited[node]
        d = dist[node]
        d_str = d if d != float('inf') else "-"
        p = prev[node] if prev[node] is not None else "-"
        print(f"  {node}   |  {vis}  |  {d_str:4} |  {p}")


if __name__ == "__main__":
    dist, prev, visited = dijkstra(graph, 'A')
    print_table(dist, prev, visited)

    path = build_path(prev, 'A', 'F')
    print("\nShortest path A -> D:", path)

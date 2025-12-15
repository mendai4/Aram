#11 Bellman Ford

def bellman_ford(n, edges, start):
    dist = [float("inf")] * n
    dist[start] = 0

    for _ in range(n - 1):
        changed = False
        for u, v, w in edges:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                changed = True
        if not changed:
            break

    for u, v, w in edges:
        if dist[u] != float("inf") and dist[u] + w < dist[v]:
            return None

    return dist

n = 5
edges = [
    (0, 1, -1), (0, 2, 4),
    (1, 2, 3),  (1, 3, 2), (1, 4, 2),
    (3, 2, 5),  (3, 1, 1),
    (4, 3, -3)
]
print(bellman_ford(n, edges, 0))
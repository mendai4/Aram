#5 BFS ցանցերում
from collections import deque

def bfs_augmenting_path(capacity, adj, s, t, parent):
    for k in parent:
        parent[k] = None
    parent[s] = s

    q = deque([s])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if parent[v] is None and capacity[u][v] > 0:
                parent[v] = u
                if v == t:
                    return True
                q.append(v)
    return False

def edmonds_karp(n, edges, s, t):
    capacity = [[0]*n for _ in range(n)]
    adj = [[] for _ in range(n)]

    for u, v, c in edges:
        capacity[u][v] += c
        if v not in adj[u]: adj[u].append(v)
        if u not in adj[v]: adj[v].append(u)

    parent = {i: None for i in range(n)}
    flow = 0

    while bfs_augmenting_path(capacity, adj, s, t, parent):
        v = t
        bottleneck = 10**18
        while v != s:
            u = parent[v]
            bottleneck = min(bottleneck, capacity[u][v])
            v = u

        v = t
        while v != s:
            u = parent[v]
            capacity[u][v] -= bottleneck
            capacity[v][u] += bottleneck
            v = u

        flow += bottleneck

    return flow

n = 6
edges = [
    (0, 1, 16), (0, 2, 13),
    (1, 2, 10), (2, 1, 4),
    (1, 3, 12), (2, 4, 14),
    (3, 2, 9),  (4, 3, 7),
    (3, 5, 20), (4, 5, 4),
]
print(edmonds_karp(n, edges, 0, 5))
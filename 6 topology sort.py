#6 Տոպոլոգիական սորտավորում
from collections import deque

def topo_sort(graph):
    indeg = {u: 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            indeg[v] = indeg.get(v, 0) + 1
            if v not in graph:
                graph[v] = []

    q = deque([u for u in indeg if indeg[u] == 0])
    order = []

    while q:
        u = q.popleft()
        order.append(u)
        for v in graph[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    if len(order) != len(indeg):
        return None
    return order

dag = {
    "A": ["C"],
    "B": ["C", "D"],
    "C": ["E"],
    "D": ["F"],
    "E": ["H", "F"],
    "F": ["G"],
    "G": [],
    "H": []
}

print(topo_sort(dag))
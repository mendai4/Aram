#7 Դեկստրայի ալգորիթմ

import heapq

def asd(graph, start):
    dist = {node: float("inf") for node in graph}
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in graph[u]:
            nd = d + w
            if nd < dist.get(v, float("inf")):
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist

wg = {
    "A": [("B", 4), ("C", 1)],
    "B": [("E", 4)],
    "C": [("B", 2), ("D", 4)],
    "D": [("E", 4)],
    "E": []
}

print(asd(wg, "A"))
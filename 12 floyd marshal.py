#12 Floyd Warshall

def floyd_warshall(n, dist):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

INF = 10**15
n = 4
dist = [
    [0,   5,  INF, 10],
    [INF, 0,   3,  INF],
    [INF, INF, 0,   1],
    [INF, INF, INF, 0],
]

ans = floyd_warshall(n, dist)
for row in ans:
    print(row)

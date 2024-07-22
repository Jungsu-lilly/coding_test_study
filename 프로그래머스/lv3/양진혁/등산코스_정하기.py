import heapq
INF = int(1e9)


def dijkstra(start):
    intensity = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heappop(q)

        if intensity < dist:
            intensity = dist

        for i in graph[now]:




def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n+1)]

    for i, j, w in range(len(paths)):
        graph[i].append([j, w])
        graph[j].append([i, w])

    for gate in gates:
        result = dijkstra(gate)


    return min_value
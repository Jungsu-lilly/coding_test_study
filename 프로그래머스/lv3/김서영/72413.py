"""
문제 설명
- positive weighted, undirected, cyclic, conntected graph
- A,B가 함께 출발하는 start node s, A,B 각 집 노드가 있을때 
- 동승하다가 각자 택시 타고 가는 상황에서 택시 요금 최소값 구하기

dijkstra 접근
- start node에서 A,B node 로의 최단 경로와 요금 최솟값 구한다.
    최단경로 매커니즘
    - heapq로 탐색 배열 만들어서 현재 정점에서 다음 정점 갈때 가장 가중치 값 작은데 우선으로 가도록 만든다.
    - distane 배열로 start에서 각 가중치까지 거리를 업데이트해나간다. 
        dsitance 배열이 inf면 아직 방문하지 않은 정점이라는 것
        계산한 거리값이 distance값보다 작으면 업데이트
    - end node 만나면 path, fare return
- 두 경로에서 겹치는 부분 가중치 한번 빼준다.

실패 분석
- start->a, start->b 각 케이스에서 최단 거리와 해당 거리 값에 해당하는 경로를 구해서 겹치는 부분은 빼주려고 했다.
- 다익스트라 알고리즘은 시작 정점으로부터 다른 모든 정점으로 가는 각 최단 거리를 구할 수 있다.
- 따라서 각 정점에 대해 경로를 구할 수 없고, 임의의 정점 x까지 최단 + x에서 a/b까지 최단 값 구해서 업데이트 하는 방식으로 가야한다.
"""

def solution(n, s, a, b, fares):
    import heapq
    # heapq is not sorted list based on the weight, 
    # this place the smallest element at the top

    graph = [[] for _ in range(n+1)]
    inf = 1e10
    for n1, n2, w in fares:
        graph[n1].append((n2, w))
        graph[n2].append((n1, w))

    def dijkstra(start: int, ends: list):
        print(f"start{start} ends{ends}")
        distance, visited, hq = [inf]*(n+1), [False]*(n+1), []
        distance[start] = 0
        heapq.heappush(hq, (0, start))

        while hq:
            cur_w, cur_n = heapq.heappop(hq)
            visited[cur_n] = True
            if cur_w > distance[cur_n]: continue

            for next_n, next_w in graph[cur_n]:
                if cur_w + next_w < distance[next_n]:
                    distance[next_n] = cur_w + next_w
                if not visited[next_n]:
                    heapq.heappush(hq, (cur_w+next_w, next_n))

        print(f"distance{distance}")
        fare = 0
        for end in ends:
            if distance[end]==inf: return None
            fare += distance[end]
        return fare

    ans = inf
    for i in range(1, n+1):
        print(i)
        if i == s: continue
        d1 = dijkstra(s, [i])
        d2 = dijkstra(i, [a, b])
        if not d1 or not d2: continue
        ans = min(ans, d1+d2)
        print(ans)

    return ans


# 4→1→5(34) 5→6(2) 5→3→2(46) 48+34=82
# n,s,a,b,fares = 6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
#14
n,s,a,b,fares = 7,3,4,1,[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
#18
# n,s,a,b,fares = 6,4,5,6,[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]
solution(n,s,a,b,fares)


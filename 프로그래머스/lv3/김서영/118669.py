"""
등산코스정하기
https://school.programmers.co.kr/learn/courses/30/lessons/118669

direction x, weight o, cycle o, connection o
intensity = 휴식없이(정점에 도달했을 때 휴식 가능) 이동해야 하는 최장시간
등산코스에서 출입구는 처음과 끝에 한 번씩, 산봉우리는 한 번만 포함
[intensity가 최소가 되는 등산코스에 포함된 산봉우리 번호, intensity 최솟값] 리턴

gate x -> summit y -> gate x
"""

def solution(n, paths, gates, summits):
    import heapq

    answer = []  # summit, intensity
    graph = [[] for _ in range(n+1)]
    for x, y, w in paths: 
        graph[x].append((y, w))
        graph[y].append((x, w))

    def dijkstra(fr, mid):
        hq = []
        intensity = 1e10
        heapq.heappush(hq, [0, fr])

        while hq:
            cur_w, cur_v = heapq.heappop()

            if cur_v == mid: return intensity
            for next_v, next_w in graph[cur_v]:
                heapq.heappush(hq, [next_w, next_v])

    for gate in gates:
        for summit in summits:
            pass

    return answer
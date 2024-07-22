# https://www.acmicpc.net/problem/

'''
1. 아이디어 :
    최단 거리를 구하기때문에 다익스트라를 사용한다.
    gates의 길이가 최대 50000이기때문에, 각 gate마다 다익스트라를 사용하면 시간초과.
    한번에 모든 gates에 대해서 연산한다.
2. 시간복잡도 :
    O( E log V)
3. 자료구조 :
    해시맵, 배열, 해시셋
'''

from collections import defaultdict
import heapq

def solution(n, paths, gates, summits):
    summits = set(summits)
    graph = defaultdict(list)
    for u, v, eff in paths:
        graph[u].append((v, eff))
        graph[v].append((u, eff))

    # dijk
    effs = [float('inf')] * (n + 1)
    queue = []
    for gate in gates:
        heapq.heappush(queue, (0, gate))
        effs[gate] = 0

    while queue:
        curr_eff, curr = heapq.heappop(queue)

        if curr in summits:
            continue
        if curr_eff > effs[curr]:
            continue

        for neighbor, eff in graph[curr]:
            max_eff = max(curr_eff, eff)
            if max_eff < effs[neighbor]:
                effs[neighbor] = max_eff
                heapq.heappush(queue, (max_eff, neighbor))

    # 최소값 찾기
    t_summit = intensity = float('inf')
    for summit in summits:
        if effs[summit] < intensity:
            t_summit = summit
            intensity = effs[summit]
        elif effs[summit] == intensity and summit < t_summit:
            t_summit = summit

    return [t_summit, intensity]

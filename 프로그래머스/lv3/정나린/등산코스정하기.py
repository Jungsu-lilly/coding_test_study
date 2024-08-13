# https://school.programmers.co.kr/learn/courses/30/lessons/118669
from collections import defaultdict
import heapq

def solution(n, paths, gates, summits):
    graph = defaultdict(list)
    for n1, n2, i in paths:
        graph[n1].append((i, n2))
        graph[n2].append((i, n1))
        
    H = [] 
    visited = [10000001] * (n + 1)
    summits.sort() # sort하는 이유: intensity가 최소가 되는 등산코스가 여거래라면, 산봉우리의 번호가 가장 낮은 코스를 리턴해야 하므로
    summit_set = set(summits)

    for gate in gates:
        heapq.heappush(H, (0, gate))
        visited[gate] = 0

    while H:
        curHighestIntensity, curNode = heapq.heappop(H)

        # 봉우리거나 curNode까지 오는 최소비용경로가 아닌 경우
        if curNode in summit_set or curHighestIntensity > visited[curNode]:
            continue

        for intensity, nextNode in graph[curNode]:
            newHighestIntensity = max(intensity, curHighestIntensity) #목표까지 가는 간선 중 가장 높은 비용을 구하기 위해
            if visited[nextNode] > newHighestIntensity: 
                #curNode -> nextNode까지 가는 간선 중 가장 큰 intensity가 visited[nextNode]에 저장되는데
                #newHighestIntensity 현재까지 가장 작은 비용인지
                visited[nextNode] = newHighestIntensity
                heapq.heappush(H, (newHighestIntensity, nextNode))

    answer = [0, 10000001] #answer[0]: 봉우리 answer[1]: 비용
    for summit in summits:
        if visited[summit] < answer[1]:
            answer[0] = summit
            answer[1] = visited[summit]

    return answer

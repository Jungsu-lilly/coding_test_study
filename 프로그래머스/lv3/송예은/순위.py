from collections import deque
# 접근 - 방향이 있는 그래프 -> 위상정렬?
# 순위가 결정된 선수는 (이전 간선 단계 + 다음 간선 단계)가 n-1인 선수
# 진입차수가 0인 노드와 해당하는 단계를 같이 넣으면서 정렬

def sort(level,graph,indegree):
    q= deque()
    
    # 초기 진입차수 0인 노드 찾기
    for i in range(1,n+1):
        if indegree[i] ==0 :
            q.append([i,0])
    
    while q:
        node,cur_level = q.popleft()
        level[node] = cur_level
        
        for i in graph[node] :
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append([i,cur_level+1])
    
def solution(n, results):
    # 진입 차수 0으로 초기화
    indegree = [0] * (n+1)
    graph = [[] for i in range(n+1)]
    level = [0] * (n+1)
    
    for a,b in results :
        indegree[b] += 1
        graph[a].append(b)
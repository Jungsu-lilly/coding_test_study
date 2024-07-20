"""lv3. 네트워크
"""
            
def solution(n, computers):
    answer = 0
    graph = {i:[] for i in range(n)}
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                graph[i].append(j)
    # print(graph)
                
    def bfs(start: int):
        q = [start]
        visit = []
        while q:
            now = q.pop(0)
            visit.append(now)
            for node in graph[now]:
                if node not in visit:
                    q.append(node)
        return visit
    
    visited = []
    for i in range(n):
        if i not in visited:
            if len(graph[i]) == 0: # network that has single node
                visited.append(i)
                answer+=1
            else:                  # find network group 
                group = bfs(i)
                visited += group
                answer +=1  
    return answer


solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])
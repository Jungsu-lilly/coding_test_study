"""
direction x, weight x, cycle o, connection x
"""
def solution(n, roads, sources, destination):
    from collections import deque
    
    graph = [[] for _ in range(n+1)]
    for fr, to in roads:
        graph[fr].append(to)
        graph[to].append(fr)
    
    def bfs(start: int) -> int:
        q = deque([(start, 0)])
        visited = set()
        while q:
            sx, sw = q.popleft()
            if sx == destination: return sw
            for nx in graph[sx]:
                if nx not in visited: 
                    visited.add(sx)
                    q.append((nx, sw+1))
        return -1
    
    answer = []
    for source in sources:
        answer.append(bfs(source))
    return answer
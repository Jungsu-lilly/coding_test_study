"""
direction x, weight x, cycle o, connection x
"""
def solution(n, roads, sources, destination):
    from collections import deque
    
    graph = [[] for _ in range(n+1)]
    for fr, to in roads:
        graph[fr].append(to)
        graph[to].append(fr)
    
    """
    시간효율
    """
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

    """
    각 source에서 destination까지 가는데 최단시간을 계산하면 중복 연산이 많을듯
    destination에서 모든 노드 최단거리 구하고 source 인덱스만 뽑아서 리턴하는게 빠르겠다
    """
    def bfs2() -> None:
        q = deque([destination])
        while q:
            sx = q.popleft()
            for nx in graph[sx]:
                if dp[nx] == -1:
                    dp[nx] = dp[sx] + 1
                    q.append(nx)

    dp = [-1 for _ in range(n+1)]
    dp[destination] = 0
    bfs2()
    return [dp[s] for s in sources]


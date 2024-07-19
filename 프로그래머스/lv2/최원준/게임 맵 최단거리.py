# https://www.acmicpc.net/problem/

'''
1. 아이디어 :
    bfs로 풀 수 있다
2. 시간복잡도 :
    O( n * m )
3. 자료구조 :
    배열
'''


from collections import deque
def solution(maps):
    visited = set()
    visited.add((0,0))
    queue = deque()
    queue.append((0,0,1)) #row, col, dist
    dir = [[0,-1],[0,1],[-1,0],[1,0]]
    while queue:
        r1, c1, dist = queue.popleft()
        if r1 == len(maps)-1 and c1 == len(maps[0])-1:
            return dist

        for r2, c2 in dir:
            nr, nc = r1+r2, c1+c2
            if not(0<=nr<len(maps) and 0<=nc<len(maps[0])) or (nr,nc) in visited or maps[nr][nc] == 0:
                continue
            visited.add((nr,nc))
            queue.append((nr,nc,dist+1))

    return -1



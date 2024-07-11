'''
1. 아이디어 :
    2차원 배열에 각 row,col 당 전 방향을 저장하는 배열을 만든다.

2. 시간복잡도 :
    O( n**2 )
3. 자료구조 :
    배열
'''

from collections import deque


def solution(board):
    n = len(board)
    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]  # right, left, down, up

    dp = [[[float('inf')] * 4 for _ in range(n)] for _ in range(n)]
    for i in range(4):
        dp[0][0][i] = 0

    queue = deque()
    queue.append([0, 0, -1, -500])  # row, col, direction, curr_cost

    while queue:
        r1, c1, d, cost = queue.popleft()
        for i in range(4):
            r2, c2 = dirs[i]
            nr, nc = r1 + r2, c1 + c2
            if not (0 <= nr < n and 0 <= nc < n) or board[nr][nc] == 1:
                continue
            ncost = cost + 100 if d == i else cost + 600
            if dp[nr][nc][i] > ncost:
                dp[nr][nc][i] = ncost
                queue.append((nr, nc, i, ncost))
    return min(dp[n - 1][n - 1])

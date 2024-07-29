from collections import deque


def solution(board):
    answer = 0
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]
    q = deque()
    v = []
    pos = [(1, 1), (1, 2)]
    q.append((pos, 0))
    v.append(pos)

    return answer
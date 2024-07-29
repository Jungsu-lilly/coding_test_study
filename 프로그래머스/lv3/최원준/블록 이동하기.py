# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

from collections import deque


def solution(board):
    n = len(board)
    dir = [[0, 1], [0, -1, ], [1, 0], [-1, 0]]

    def moveable_check(x, y):
        return 0 <= x < n and 0 <= y < n and board[x][y] == 0

    def get_next_positions(x1, y1, x2, y2):
        next_positions = []

        for dx, dy in dir:  # 상하좌우 이동
            nx1, ny1, nx2, ny2 = x1 + dx, y1 + dy, x2 + dx, y2 + dy
            if moveable_check(nx1, ny1) and moveable_check(nx2, ny2):
                next_positions.append((nx1, ny1, nx2, ny2))

        if x1 == x2:  # 가로 회전
            for d in [-1, 1]:
                if moveable_check(x1 + d, y1) and moveable_check(x2 + d, y2):
                    next_positions.append((x1, y1, x1 + d, y1))
                    next_positions.append((x2, y2, x2 + d, y2))

        if y1 == y2:  # 세로 회전
            for d in [-1, 1]:
                if moveable_check(x1, y1 + d) and moveable_check(x2, y2 + d):
                    next_positions.append((x1, y1, x1, y1 + d))
                    next_positions.append((x2, y2, x2, y2 + d))
        return next_positions

    queue = deque()
    queue.append(((0, 0, 0, 1), 0))
    visited = set()
    visited.add((0, 0, 0, 1))

    while queue:
        (x1, y1, x2, y2), time = queue.popleft()

        if (x1, y1) == (n - 1, n - 1) or (x2, y2) == (n - 1, n - 1):
            return time

        for next_position in get_next_positions(x1, y1, x2, y2):
            if next_position in visited:
                continue
            visited.add(next_position)
            queue.append((next_position, time + 1))

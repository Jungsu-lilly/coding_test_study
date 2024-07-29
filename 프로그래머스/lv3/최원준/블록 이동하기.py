# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


from collections import deque
def solution(board):
    n = len(board)-1

    def moveable_check(x1, y1):
        return 0<=x1<n and 0<=y1<n and board[x1][y1] == 0

    def rotate_check(row, col):
        if moveable_check(row+1, col) and moveable_check(row+1, col+1):
            return True
        if moveable_check(row-1, col-1) and moveable_check(row-1, col) and moveable_check(row-1, col+1) and moveable_check(row, col-1) and moveable_check(row+1, col-1) and moveable_check(row+1, col):
            return True

    dir = [[0,1],[1,0]]

    dp = [[[False, False] for _ in range(len(board)-1)] for _ in range(len(board)-1)] #hor, ver
    dp[0][0][0] = True

    queue = deque()
    queue.append((0,0,0))

    while queue:
        row1, col1, is_ver = queue.popleft()
        print(row1, col1, is_ver)

        if not is_ver and rotate_check(row1, col1):
            dp[row1][col1][1] = True
            queue.append((row1, col1, 1))
        for row2, col2 in dir:
            nrow, ncol = row1+row2, col1+col2
            if not moveable_check(nrow, ncol):
                continue
            if is_ver and not moveable_check(nrow, ncol+1):
                continue
            elif not is_ver and not moveable_check(nrow+1, ncol):
                continue
            dp[nrow][ncol][is_ver] = True
            queue.append((nrow, ncol, is_ver))

    print(*dp, sep='\n')
    return





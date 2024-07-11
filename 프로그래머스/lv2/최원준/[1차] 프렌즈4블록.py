'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''

def solution(m, n, board):

    def move_down(board):
        for col in range(n):
            stack = []
            for row in range(m):
                if board[row][col] != '@':
                    stack.append(board[row][col])
            for row in range(m - 1, -1, -1):
                if stack:
                    board[row][col] = stack.pop()
                else:
                    board[row][col] = '@'

    def check_four(board):
        counter = set()
        for row in range(m - 1):
            for col in range(n - 1):
                base = board[row][col]
                if base != '@' and base == board[row + 1][col] == board[row][col + 1] == board[row + 1][col + 1]:
                    counter.add((row, col))
                    counter.add((row + 1, col))
                    counter.add((row, col + 1))
                    counter.add((row + 1, col + 1))
        for row, col in counter:
            board[row][col] = '@'
        return len(counter)

    board = [list(row) for row in board]

    ans = 0
    while True:
        delete_count = check_four(board)
        if delete_count == 0:
            break
        ans += delete_count
        move_down(board)

    return ans
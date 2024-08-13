# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


def solution(board):
    def check_row(row):
        if board[row][0] != ".":
            return board[row][0] == board[row][1] == board[row][2]
        return False

    def check_col(col):
        if board[0][col] != ".":
            return board[0][col] == board[1][col] == board[2][col]
        return False

    def check_diag():
        if board[1][1] != ".":
            return board[0][0] == board[1][1] == board[2][2]
        return False

    def check_diag_r():
        if board[1][1] != ".":
            return board[2][0] == board[1][1] == board[0][2]
        return False

    Os = Xs = 0

    # check_count
    for row in range(3):
        for col in range(3):
            if board[row][col] == "O":
                Os += 1
            elif board[row][col] == "X":
                Xs += 1
    if Xs > Os or Os > 5 or Xs > 4 or Os > Xs + 1:
        print(1)
        return 0

    finished = False
    winner = None
    for i in range(3):
        if check_row(i):
            if finished and winner != board[i][1]:
                print(2)
                return 0
            finished = True
            winner = board[i][1]
        if check_col(i):
            if finished and winner != board[1][i]:
                print(3)
                return 0
            finished = True
            winner = board[1][i]

    if check_diag():
        if finished and winner != board[1][1]:
            print(4)
            return 0
        finished = True
        winner = board[1][1]
    if check_diag_r():
        if finished and winner != board[1][1]:
            print(5)
            return 0
        finished = True
        winner = board[1][1]

    if winner == "O" and Xs != Os - 1:
        return 0
    if winner == "X" and Xs != Os:
        return 0
    return 1

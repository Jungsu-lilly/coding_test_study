def win(board):
    winner = []
    for i in board:
        if 1 == len(set(i)):
            winner.append(set(i))

    for i in range(3):
        tmp = ''
        for j in range(3):
            tmp += board[j][i]

        if 1 == len(set(tmp)):
            winner.append(set(tmp))

    if (1 == len(set([board[0][0], board[1][1], board[2][2]]))):
        winner.append(set([board[0][0], board[1][1], board[2][2]]))

    if (1 == len(set([board[0][2], board[1][1], board[2][0]]))):
        winner.append(set([board[0][2], board[1][1], board[2][0]]))
    return winner


def solution(board):
    x_cnt = 0
    o_cnt = 0

    board = [list(row) for row in board]

    for i in range(len(board)):
        for j in range(len(board[i])):
            if "X" == board[i][j]:
                x_cnt += 1
            if "O" == board[i][j]:
                o_cnt += 1

    winner = win(board)

    if x_cnt > o_cnt:
        return 0

    if o_cnt == x_cnt:
        return 0

    if len(winner) == 2:
        return 0

    if (set(winner) == "O") and (o_cnt != x_cnt + 1):
        return 0

    if (set(winner) == "X") and (o_cnt != x_cnt):
        return 0

    return 1





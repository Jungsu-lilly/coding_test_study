#

'''
1. 아이디어 :
    누적합
2. 시간복잡도 :
    O(nm)
3. 자료구조 :
    배열
'''


def solution(board, skill):
    row = len(board)
    col = len(board[0])

    csum = [[0 for _ in range(col + 1)] for _ in range(row + 1)]

    count = 0

    for t, row1, col1, row2, col2, degree in skill:
        if t == 1:  # 공격
            degree *= -1

        csum[row1][col1] += degree #합 시작점
        csum[row1][col2 + 1] -= degree #가로(오른쪽)합 끝지점
        csum[row2 + 1][col1] -= degree #세로(아래)합 끝지점
        csum[row2 + 1][col2 + 1] += degree # 가로 세로 두번 더해지기떄문에 한번 뺴서 0으로 만든다.

    for row in range(len(csum)): #가로 누적합
        for col in range(1, len(csum[0])):
            csum[row][col] = csum[row][col - 1] + csum[row][col]

    for col in range(len(csum[0])): #세로 누적합
        for row in range(1, len(csum)):
            csum[row][col] = csum[row - 1][col] + csum[row][col]

    for row in range(len(board)): # 초기 board와 비교
        for col in range(len(board[0])):
            if board[row][col] + csum[row][col] >= 1:
                count += 1

    return count

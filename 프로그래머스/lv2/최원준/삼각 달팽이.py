# https://www.acmicpc.net/problem/

'''
1. 아이디어 :
    구현
2. 시간복잡도 :
    O( n! )
3. 자료구조 :
    배열
'''

def solution(n):
    total_rows = n
    tower = [[0 for _ in range(n)] for _ in range(n)]
    dir = 0
    count = 1
    row = -1
    col = 0
    while n:
        if dir == 0:
            for i in range(n):
                row += 1
                tower[row][col] = count
                count += 1
        elif dir == 1:
            for i in range(n):
                col += 1
                tower[row][col] = count
                count += 1
        elif dir == 2:
            for i in range(n):
                row -= 1
                col -= 1
                tower[row][col] = count
                count += 1
        n -= 1
        dir = (dir + 1) % 3

    ans = []
    for row in range(total_rows):
        for col in range(row+1):
            ans.append(tower[row][col])
    return ans

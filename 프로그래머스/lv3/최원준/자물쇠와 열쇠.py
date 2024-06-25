'''
1. 아이디어 :
    구현문제
2. 시간복잡도 :
    O( n**2 * m**2 )
3. 자료구조 :
    배열

'''

def solution(key, lock):
    def rotate_key():
        n = len(key)
        for j in range(n // 2):
            for i in range(n - 1 - 2 * j):
                key[j][j + i], key[j + i][n - 1 - j], key[n - 1 - j][n - 1 - j - i], key[n - 1 - j - i][j] = key[n - 1 - j - i][j], key[j][j + i], key[j + i][n - 1 - j], key[n - 1 - j][n - 1 - j - i]


    def check(x, y, total):
        n = len(lock)
        m = len(key)
        for row in range(m):
            for col in range(m):
                if 0 <= x + row < n and 0 <= y + col < n:
                    if key[row][col] == 1 and lock[x + row][y + col] == 1:
                        return False
                    if key[row][col] == 1 and lock[x + row][y + col] == 0:
                        total -= 1
        return total == 0

    holes = 0
    for row in range(len(lock)):
        for col in range(len(lock)):
            if lock[row][col] == 0:
                holes += 1

    for row in range(-len(key)+1, len(lock)):
        for col in range(-len(key)+1, len(lock)):
            for i in range(4):
                if check(row, col, holes):
                    return True
                rotate_key()
    return False
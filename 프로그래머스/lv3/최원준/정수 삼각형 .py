# https://www.acmicpc.net/problem/

'''
1. 아이디어 :
    dp로 풀 수 있다.
2. 시간복잡도 :
    O(n*m)
3. 자료구조 :
    -
'''


def solution(triangle):
    size = len(triangle)

    for row in range(1, size):
        triangle[row][0] += triangle[row - 1][0]  # 가장 왼쪽
        for col in range(1, row):
            triangle[row][col] += max(triangle[row - 1][col - 1], triangle[row - 1][col])
        triangle[row][-1] += triangle[row - 1][-1]  # 가장 오른쪽
    return max(triangle[-1])

def solution(triangle):
    size = len(triangle)
    for row in range(size-2,-1,-1):
        for col in range(row+1):
            triangle[row][col] += max(triangle[row+1][col], triangle[row+1][col+1])
    return triangle[0][0]
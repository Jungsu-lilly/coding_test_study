# https://school.programmers.co.kr/learn/courses/30/lessons/12949
def solution(arr1, arr2):
    m = len(arr1)
    n = len(arr2[0])
    r = len(arr1[0])
    matrix = [[0] * n for _ in range(m)]
    for i in range(m):  
        for j in range(n):
            for k in range(r):
                matrix[i][j] += arr1[i][k] * arr2[k][j]
    return matrix

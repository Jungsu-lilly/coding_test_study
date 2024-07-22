"""
행렬의 곱셈
https://school.programmers.co.kr/learn/courses/30/lessons/12949
"""

def solution(arr1, arr2):
    # len(arr1)*len(arr1[0])  *  len(arr2)*len(arr2[0])
    # len(arr1)  *  len(arr2[0])
    n, l, m = len(arr1), len(arr1[0]), len(arr2[0])
    answer = [[0 for _ in range(m)] for _ in range(n)]
    
    def plain(answer):
        for i in range(n):
            for j in range(m):
                for k in range(l):
                    answer[i][j] += arr1[i][k] * arr2[k][j]
        return answer
    
    def transpose(answer):
        t_arr2 = list(zip(*arr2))
        for i, row in enumerate(arr1):
            for j, col in enumerate(t_arr2):
                answer[i][j] += sum(x*y for x, y in zip(row, col))
        return answer
                
    return transpose(answer)
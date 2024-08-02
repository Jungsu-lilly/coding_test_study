"""
산 모양 타일링
https://school.programmers.co.kr/learn/courses/30/lessons/258705
"""


def solution(n, tops):
    a, b = [0]*(n), [0]*(n)
    a[0] = 1
    b[0] = 3 if tops[0] else 2
    
    for k in range(1, n):
        a[k] = a[k-1] + b[k-1]
        b[k] = a[k-1]*(tops[k]+1) + b[k-1]*(tops[k]+2)
    return (a[-1]+b[-1])%10007

solution(4, [1, 1, 0, 1])
solution(2, [0, 1])
solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
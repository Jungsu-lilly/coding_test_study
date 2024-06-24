'''
1. 아이디어 :
    dp
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    -
'''

def solution(n):
    p1, p2 = 1, 2
    for i in range(n-2):
        p1, p2 = p2, p1 + p2
    return p2%1234567 if n>=2 else p1
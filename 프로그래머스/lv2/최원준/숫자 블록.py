# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


import sys
#sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def solution(begin, end):
    answer = []

    def calc(n):
        if n == 1:
            return 0
        cmax = 1
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                if n // i <= 10000000:
                    return n//i
                else:
                    cmax = i
        return cmax

    for i in range(begin, end+1):
        answer.append(calc(i))
    return answer

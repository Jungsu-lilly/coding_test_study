# https://www.acmicpc.net/problem/

'''
1. 아이디어 :
    union-find르 사용
2. 시간복잡도 :
    O(n**2)
3. 자료구조 :
    배열
'''

from collections import defaultdict


def solution(n, computers):
    def find(x):
        if x != par[x]:
            par[x] = find(par[x])
        return par[x]

    def union(a, b):
        ra = find(a)
        rb = find(b)
        if ra == rb:
            return True

        if rank[ra] > rank[rb]:
            par[rb] = ra
        elif rank[ra] < rank[rb]:
            par[ra] = rb
        else:
            par[rb] = ra
            rank[ra] += 1
        return False

    par = [i for i in range(n)]
    rank = [1 for _ in range(n)]

    ans = 0
    for start in range(n):
        for end in range(n):
            if start == end or computers[start][end] == 0:
                continue
            if not union(start, end):
                ans += 1
    return n - ans

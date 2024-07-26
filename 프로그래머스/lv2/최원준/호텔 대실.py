# https://www.acmicpc.net/problem/155651

'''
1. 아이디어 :
    interval문제. 스택 사용
2. 시간복잡도 :
    O( nlogn )
3. 자료구조 :
    힙
'''

import heapq


def solution(book_time):
    def serialize(t):
        h, m = t.split(":")
        return int(h) * 60 + int(m)

    book_time = sorted([[serialize(start), serialize(end) + 10] for start, end in book_time])
    stack = []
    cmax = 0

    for start, end in book_time:
        while stack and stack[0] <= start:
            heapq.heappop(stack)
        heapq.heappush(stack, end)
        cmax = max(cmax, len(stack))
    return cmax

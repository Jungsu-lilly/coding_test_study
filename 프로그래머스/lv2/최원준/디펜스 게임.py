# https://www.acmicpc.net/problem/

'''
1. 아이디어 :
    힙
2. 시간복잡도 :
    O( nlogn )
3. 자료구조 :
    최대힙
'''

import heapq


def solution(n, k, enemy):
    max_heap = []
    idx = 0
    while idx < len(enemy) and n >= 0:
        heapq.heappush(max_heap, -enemy[idx])
        n -= enemy[idx]
        if n < 0:
            if k:
                k -= 1
                n -= heapq.heappop(max_heap)
            else:
                return idx
        # print(max_heap, n, idx)
        idx += 1
    return idx

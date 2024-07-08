'''
1. 아이디어 :
    union-find 문제
2. 시간복잡도 :
    O( nlogn )
3. 자료구조 :
    배열
'''

import heapq
def solution(n, costs):

    def find(x):
        if par[x] != x:
            par[x] = find(par[x])
        return par[x]

    def union(a, b):
        ra = find(a)
        rb = find(b)
        if ra == rb:
            return False

        if rank[ra] > rank[rb]:
            par[rb] = ra
        elif rank[rb] < rank[ra]:
            par[ra] = rb
        else:
            par[rb] = ra
            rank[ra] += 1
        return True

    costs = [[costs[i][2], costs[i][0], costs[i][1]] for i in range(len(costs))]
    heapq.heapify(costs)
    par = [i for i in range(n)]
    rank = [1 for i in range(n)]
    total = 0

    while costs:
        cost, a, b = heapq.heappop(costs)
        if union(a,b):
            total += cost

    return total

# https://www.acmicpc.net/problem/

'''
1. 아이디어 :
    최단 가격을 구하려면 각자 타고가거나, 어느 중간 지점까지 같이 타고가야한다.
    플로이드-워셜을 통해 모든 지점부터 모든 지점까지의 최소값을 구한다.
    임의의 중간지점(mid)를 선택하고, s->mid + mid->a + mid->b 한다
2. 시간복잡도 :
    O( n**3 )
3. 자료구조 :
    배열
'''

from collections import defaultdict


def solution(n, s, a, b, fares):
    s, a, b = s - 1, a - 1, b - 1
    dp = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0
    for u, v, c in fares:
        dp[u - 1][v - 1] = c
        dp[v - 1][u - 1] = c

    for mid in range(n):
        for start in range(n):
            for end in range(n):
                if dp[start][end] > dp[start][mid] + dp[mid][end]:
                    dp[start][end] = dp[start][mid] + dp[mid][end]

    ans = float('inf')
    for mid in range(n):
        ans = min(ans, dp[s][mid] + dp[mid][a] + dp[mid][b])
    return ans

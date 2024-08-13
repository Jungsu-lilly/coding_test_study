# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


def solution(n):
    # n = 20
    if n%2 == 1:
        return 0
    MOD = 1000000007
    dp = [1] * (n+1)
    dp[2] = 3
    # dp[4] = 3*3 + 2 = 11
    # dp[6] = 11*3 + dp[0]*2 + dp[2]*2 = 33 + 2 + 6 = 41
    # dp[8] = 41*3 + dp[0]*2 + dp[2]*2 + dp[4]*2 = 123 + 2 + 6 + 22 = 153
    # dp[10] = 153*3 + dp[0]*2 + dp[2]*2 + dp[4]*2 + dp[6]*2 = 459 + 2 + 6 + 22 + 82 = 571
    for i in range(4, n + 1, 2):
        dp[i] = (dp[i-2] * 3) % MOD
        for j in range(0, i-2, 2):
            dp[i] += (dp[j] * 2) % MOD

    return dp[n] % MOD
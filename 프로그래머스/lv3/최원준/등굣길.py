# https://www.acmicpc.net/problem/

'''
1. 아이디어 :
    puddle은 n,m이 아닌, m,n.
    dp로 풀수 있다
    dp[row][col] = (dp[row-1][col] + dp[row][col-1]) % 1000000007
2. 시간복잡도 :
    O( n * m )
3. 자료구조 :
    배열
'''


def solution(m, n, puddles):
    dp = [[0 for _ in range(m)] for _ in range(n)]
    puddles = set((col-1,row-1) for row, col in puddles)

    dp[0][0] = 1
    for i in range(1, n):
        if (i, 0) in puddles:
            break
        dp[i][0] = dp[i-1][0]
    for i in range(1, m):
        if (0, i) in puddles:
            break
        dp[0][i] = dp[0][i-1]

    for row in range(1,n):
        for col in range(1,m):
            if (row, col) in puddles:
                continue
            dp[row][col] = (dp[row-1][col] + dp[row][col-1]) % 1000000007

    return dp[-1][-1]
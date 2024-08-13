def solution(s):
    n = len(s)
    dp = [[ False for _ in range(n)] for _ in range(n)]
    ans = (0, 0)
    for i in range(n): dp[i][i] = True
    # diff 1 체크
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            ans = (i, i+1)
    # diff > 1 체크
    for diff in range(2, n):
        # i, i+diff 범위를 확인하면서
        # 해당 범위 포인트의 문자열이 같고, 그 바로 안쪽 범위 문자열이 palin인지 확인
        for i in range(n-diff):
            j = i + diff
            if s[i] == s[j] and dp[i+1][j-1]:
                dp[i][j] = True
                ans = (i, j)
    i, j = ans
    return j-i+1



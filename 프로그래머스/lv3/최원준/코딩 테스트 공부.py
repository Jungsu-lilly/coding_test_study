# https://www.acmicpc.net/problem/

'''
1. 아이디어 :
    dp 문제
2. 시간복잡도 :
    O( max_alp * max_cop * problems)
3. 자료구조 :
    배열
'''


def solution(alp, cop, problems):
    max_alp = max([problem[0] for problem in problems])
    max_cop = max([problem[1] for problem in problems])

    dp = [[float('inf')] * (max_cop + 1) for _ in range(max_alp + 1)]  # dp[alp][cop] = time
    alp, cop = min(alp, max_alp), min(cop, max_cop)
    dp[alp][cop] = 0

    for alp_score in range(alp, max_alp + 1):
        for cop_score in range(cop, max_cop + 1):
            if alp_score + 1 <= max_alp:  # +1 alp
                dp[alp_score + 1][cop_score] = min(dp[alp_score + 1][cop_score], dp[alp_score][cop_score] + 1)
            if cop_score + 1 <= max_cop:  # +1 cop
                dp[alp_score][cop_score + 1] = min(dp[alp_score][cop_score + 1], dp[alp_score][cop_score] + 1)

            for problem in problems:
                nalp, ncop, palp, pcop, time = problem

                if alp_score >= nalp and cop_score >= ncop:
                    ni = min(max_alp, alp_score + palp)
                    nj = min(max_cop, cop_score + pcop)
                    dp[ni][nj] = min(dp[ni][nj], dp[alp_score][cop_score] + time)

    return dp[max_alp][max_cop]

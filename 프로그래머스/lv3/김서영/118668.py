"""
코딩 테스트 공부
https://school.programmers.co.kr/learn/courses/30/lessons/118668
"""

def solution(alp, cop, problems):
    """
    처음 접근 방식 - problems linear search하면서 다음 알고력/코딩력 채우고 넘어가는 식
    경우의 수가 너무 많아진다. 다 케이스로 if처리를 하는것보다 1씩 올리면서 dp/dfs/bfs 탐색을 해야함
    """
    import math
    answer = 0
    n = len(problems)
    
    alp_goal = max([problems[i][0] for i in range(n)])
    cop_goal = max([problems[i][1] for i in range(n)])
    problems.sort(key=lambda x: (abs(x[0]-alp)+abs(x[1]-cop), x[4]))
    
    for i, (alp_req, cop_req, alp_rwd, cop_rwd, cost) in enumerate(problems):
        # 목표 알고력, 코딩력 확인
        if alp >= alp_goal and cop >=cop_goal: return answer
    
        # 현재 문제 푸는데 필요한 알고력, 코딩력 채우기
        if alp<alp_req or cop<cop_req: 
            answer += max(0, alp_req-alp) + max(0, cop_req-cop)
            alp = max(alp, alp_req)
            cop = max(cop, cop_req)
        # 다음 문제 푸는데 필요한만큼 현재 문제 풀기
        if i<n-1:
            solve_time = max(math.ceil((problems[i+1][0]-alp)/alp_rwd), math.ceil((problems[i+1][1]-cop)/cop_rwd))
            alp+=alp_rwd*solve_time
            cop+=cop_rwd*solve_time
            answer+=cost*solve_time
        
                
    return answer


def solution_dp(alp, cop, problems):
    n = len(problems)
    alp_goal = max([problems[i][0] for i in range(n)])
    cop_goal = max([problems[i][1] for i in range(n)])
    print(problems, alp_goal, cop_goal)

    # dp[alp][cop] = time 저장하는 dp배열 선언
    dp = [[1e10] * (cop_goal + 1) for _ in range(alp_goal + 1)]  
    dp[alp][cop] = 0

    for cur_alp in range(alp, alp_goal+1):
        for cur_cop in range(cop, cop_goal+1):
            cur_time = dp[cur_alp][cur_cop]
            # 알고력, 코딩력 각각 하나씩 올려보고 해당 위치 dp에 time값 갱신
            if cur_alp+1 <= alp_goal: 
                dp[cur_alp+1][cur_cop] = min(cur_time+1, dp[cur_alp+1][cur_cop])
            if cur_cop+1 <= cop_goal: 
                dp[cur_alp][cur_cop+1] = min(cur_time+1, dp[cur_alp][cur_cop+1])

            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if cur_alp >= alp_req and cur_cop >= cop_req:
                    i = min(cur_alp+alp_rwd, alp_goal)
                    j = min(cur_cop+cop_rwd, cop_goal)
                    dp[i][j] = min(dp[i][j], cur_time+cost)
            
    print('\n', dp)
    return dp[alp_goal][cop_goal]

solution_dp(10, 10, [[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]])
solution_dp(0, 0, [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]])

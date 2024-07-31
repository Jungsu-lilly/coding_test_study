def solution(alp, cop, problems):
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

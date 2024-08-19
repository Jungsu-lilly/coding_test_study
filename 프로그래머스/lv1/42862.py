def solution(n, lost, reserve):    
    clothes = [1] * (n + 1)
    answer = 0
    
    for i in lost:
        clothes[i] -= 1
    for i in reserve:
        clothes[i] += 1
        
    for i in clothes:
        if i >= 1: answer += 1
    answer -= 1 # 0번째 제외
        
    for i in range(1, n+1): # 인덱스: 1 ~ n
        if clothes[i] == 0: # i 번째 학생이 체육복이 없음 : 앞, 뒤 확인
            if i-1 >= 1 and clothes[i-1] > 1:
                clothes[i-1] -= 1
                answer += 1
                continue
            elif i+1 <= n and clothes[i+1] > 1:
                clothes[i+1] -= 1
                answer += 1
    
    return answer

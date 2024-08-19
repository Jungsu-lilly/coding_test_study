def solution(a):
    d = dict()  # {숫자:개수}
    
    for i in a:
        if i not in d: 
            d[i] = 1
        else:
            d[i] += 1
            
    ans = -1 # 공통 원소가 얼만큼 사용됐는지
    
    for k in d:
        if d[k] <= ans: # k 등장횟수가 정답보다 작으면, 계산할 필요 X
            continue
        idx = 0
        tmp = 0
        
        while idx < len(a) - 1:
            # a[idx], a[idx+1] 둘 다 k가 없으면 공통값 k가 없음
            # a[idx] == a[idx+1] : 집합 내의 숫자들이 달라야 함 (문제 조건 위배)
            if (a[idx] != k and a[idx+1] != k) or (a[idx] == a[idx+1]):
                idx += 1
                continue
            
            # 스타수열 원소로 추가
            tmp += 1
            idx += 2
            
        ans = max(ans, tmp)
        
    if ans == -1:
        return 0
    
    return ans * 2

def solution(lottos, win_nums):
    zero_cnt, cnt = 0, 0
    visited = [0] * 6
    for i in lottos:
        if i == 0: zero_cnt += 1
        
    tmp = zero_cnt
    
    for i in win_nums:
        for j in range(6):
            if lottos[j] == i and visited[j] == 0:
                cnt += 1
                visited[j] = 1
                continue
            if tmp > 0:
                tmp -= 1
                cnt += 1
                
    result = []
    if cnt < 2: 
        result.append(6)
        result.append(6)
    else:
        result.append(7-cnt)
        if cnt-zero_cnt <= 1: result.append(6)
        else: result.append(7-(cnt-zero_cnt))
        
    return result

def solution(lottos, win_nums):
    answer = []

    zero_cnt = 0
    right_lottos = 0
    same_num = 0  
    
    for lotto in lottos:
        if lotto in win_nums: #right_lottos = sum(1 for lotto in lottos if lotto in win_nums)    
            right_lottos += 1
        if lotto == 0: # zero_cnt = lottos.count(0)
            zero_cnt += 1
    # 하나도 일치하지 않다면 7순위가 아닌 6순위 return
    max_sum = 7-(right_lottos+zero_cnt) if right_lottos+zero_cnt > 0 else 6
    min_sum = 7-right_lottos if right_lottos > 0 else 6
    
    answer.append(max_sum)
    answer.append(min_sum)

    # [최고 순위, 최저 순위]
    return answer
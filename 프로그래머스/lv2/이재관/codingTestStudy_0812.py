def solution(lottos, win_nums):
    answer = []
    cnt = 0
    zero_num = lottos.count(0)

    def check_rank(x):
        rank = 0
        if x == 6:
            rank = 1
        elif x == 5:
            rank = 2
        elif x == 4:
            rank = 3
        elif x == 3:
            rank = 4
        elif x == 2:
            rank = 5
        else:
            rank = 6
        return rank

    for i in lottos:
        if i in win_nums:
            cnt += 1

    max_cnt = cnt + zero_num

    answer = [check_rank(max_cnt), check_rank(cnt)]

    return answer




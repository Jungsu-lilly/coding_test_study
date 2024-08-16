# https://school.programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    answer = []
    common_num = len([i for i in lottos if i in win_nums])
    zero_num = lottos.count(0)
    answer.append(7-common_num-zero_num if 7-common_num-zero_num < 7 else 6)
    answer.append(7-common_num if 7-common_num < 7 else 6)
    return answer

solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])
solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25])
solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35])

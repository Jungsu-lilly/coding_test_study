# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


def solution(lottos, win_nums):
    prize = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    win_nums = set(win_nums)
    zero = match = 0
    for n in lottos:
        zero = zero+1 if n == 0 else zero
        match = match+1 if n in win_nums else match

    return [prize[match + zero], prize[match]]

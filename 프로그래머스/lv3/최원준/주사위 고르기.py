# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

from itertools import combinations
from collections import defaultdict


def solution(dice):
    def calc_sum(comb):  # 모든 조합
        sums = defaultdict(int)

        def dfs(index, curr):
            if index == len(comb):
                sums[curr] += 1
                return
            for value in comb[index]:
                dfs(index + 1, curr + value)

        dfs(0, 0)
        return sums

    def calc_win(A_dice, B_dice):  # 점수 계산
        winA = 0
        candidsA, candidsB = calc_sum(A_dice), calc_sum(B_dice)

        for candidA, countA in candidsA.items():
            for candidB, countB in candidsB.items():
                if candidA > candidB:
                    winA += countA * countB
        return winA

    n = len(dice)
    max_dices = n // 2
    combs = list(combinations(range(n), max_dices))
    cmax = -1
    ans = None

    for combA in combs:
        combA = set(combA)
        combB = [i for i in range(n) if i not in combA]
        dicesA, dicesB = [dice[i] for i in combA], [dice[i] for i in combB]

        winA = calc_win(dicesA, dicesB)

        if winA > cmax:
            cmax = winA
            ans = combA

    return sorted([i + 1 for i in ans])

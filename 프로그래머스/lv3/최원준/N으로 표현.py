# https://www.acmicpc.net/problem/

'''
1. 아이디어 :
    dp문제
    N 4개로 만들 수 있는 조합은, N 1개 +-*/ N 3개, N 2개 +-*/ N 2개, N 3개 +-*/ N 1개
    숫자를 이어붙일수도 있으므로, 초기화할때 같이 넣어준다.
2. 시간복잡도 :
    O(n*n*9*9)
3. 자료구조 :
    해시셋, 배열
'''


def solution(N, number):
    if N == number:
        return 1

    def get_combinations(set1, set2):
        ans = set()
        for num1 in set1:
            for num2 in set2:
                ans.add(num1 + num2)
                ans.add(num1 - num2)
                ans.add(num1 * num2)
                if num2 != 0:
                    ans.add(num1 // num2)
        return ans

    dp = [set() for _ in range(9)]

    for i in range(1,9):
        dp[i].add(int(str(N) * i))

    for i in range(1, 9):
        for j in range(1, i):
            left_part = dp[j]
            right_part = dp[i-j]
            dp[i].update(get_combinations(left_part, right_part))
        if number in dp[i]:
            return i
    return -1
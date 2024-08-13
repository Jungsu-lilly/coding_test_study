# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


def solution(s):
    left = 0
    right = 1
    ans = 0
    while left < len(s):
        ans += 1
        base = s[left]
        base_count = 1
        diff_count = 0
        while right < len(s) and base_count != diff_count:
            if s[right] == base:
                base_count += 1
            else:
                diff_count += 1
            right += 1
        left = right
        right += 1

    return ans

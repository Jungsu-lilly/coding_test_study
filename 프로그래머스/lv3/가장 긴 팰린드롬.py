# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


def solution(s):
    size = len(s)

    def get_pal(left, right):
        length = 0
        while left>=0 and right<size:
            if s[left] == s[right]:
                length += 2
                left -=1
                right += 1
            else:
                break
        return length

    ans = 0
    for i in range(len(s)):
        ans = max(ans, get_pal(i,i) - 1)
        ans = max(ans, get_pal(i, i+1))


    return ans

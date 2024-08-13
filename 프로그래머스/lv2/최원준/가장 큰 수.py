# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


def solution(numbers):
    def converted(x):
        return int(str(x)*3)

    nums = sorted(numbers, key=lambda x: str(converted(x)), reverse=True)
    return str(int("".join(str(n) for n in nums)))
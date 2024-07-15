# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


from collections import defaultdict
def solution(numbers, target):
    prev = defaultdict(int)
    prev[0] = 1

    for i, n in enumerate(numbers):
        curr = defaultdict(int)
        for k, v in prev.items():
            curr[k+n] += v
            curr[k-n] += v
        prev = curr
    return prev[target]

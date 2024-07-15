# https://www.acmicpc.net/problem/

'''
1. 아이디어 :
    해당 숫자를 더하거나 뺀 결과를 저장하고, 저장된 결과에서 또 더하고 뺴고를 반복
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    해시맵
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

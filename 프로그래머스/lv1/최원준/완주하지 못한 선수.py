# https://www.acmicpc.net/problem/

'''
1. 아이디어 :
    -
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    해시맵
'''

from collections import Counter
def solution(participant, completion):
    c = Counter(participant)
    for p in completion:
        if c[p] == 0:
            return p
        c[p] -= 1
    for k, v in c.items():
        if v != 0:
            return k

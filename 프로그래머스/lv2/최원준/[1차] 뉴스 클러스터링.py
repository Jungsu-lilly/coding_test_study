# https://www.acmicpc.net/problem/

'''
1. 아이디어 :
    2개씩 끊어서 유효하면 카운터(c1, c2)에 추가.
    c1 키:값을 순해하면서 키가 c2에 존재하면 anb는 min을 저장, aub는 max를 저장하고 존재하지 않으면 aub에 값을 저장.
    c2도 반복한다.
    anb 값들의 합 / aub 값들의 합 * 65536
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    해시맵
'''

from collections import defaultdict
from collections import Counter


def solution(str1, str2):
    def valid(s):
        return 97 <= ord(s[0]) <= 122 and 97 <= ord(s[1]) <= 122

    # 2개씩 끊어서 유효하면 카운터에 추가
    str1, str2 = str1.lower(), str2.lower()
    c1 = Counter([str1[i] + str1[i + 1] for i in range(len(str1) - 1) if valid(str1[i] + str1[i + 1])])
    c2 = Counter([str2[i] + str2[i + 1] for i in range(len(str2) - 1) if valid(str2[i] + str2[i + 1])])
    if not c1 and not c2:
        return 65536

    anb = defaultdict(int)
    aub = defaultdict(int)

    for k, v in c1.items():
        if k in c2:
            anb[k] = min(c1[k], c2[k])
            aub[k] = max(c1[k], c2[k])
        else:
            aub[k] += v
    for k, v in c2.items():
        if k in c1:
            anb[k] = min(c1[k], c2[k])
            aub[k] = max(c1[k], c2[k])
        else:
            aub[k] += v

    return int(sum(anb.values()) / sum(aub.values()) * 65536)

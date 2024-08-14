# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


from collections import defaultdict
def solution(s, skip, index):
    skip = set(list(skip))
    alpha_map1 = {}
    alpha_map2 = {}

    idx = 0
    for i in range(26):
        if chr(i+97) in skip:
            continue
        alpha_map1[idx] = chr(i+97)
        alpha_map2[chr(i+97)] = idx
        idx+=1

    MOD = len(alpha_map1)
    s = list(s)
    for i, c in enumerate(s):
        curr_idx = alpha_map2[c]
        next_char = alpha_map1[(curr_idx+index)%MOD]
        s[i] = next_char

    return "".join(s)
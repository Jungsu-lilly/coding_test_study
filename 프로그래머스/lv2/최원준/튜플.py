# https://www.acmicpc.net/problem/

'''
1. 아이디어 :
    변환 작업합니다
2. 시간복잡도 :
    O(nlogn)
3. 자료구조 :
    배열, 해시셋
'''


def solution(s):
    s = sorted(s[2:-2].split("},{"), key = lambda x: len(x))
    #	['2', '2,1', '2,1,3', '2,1,3,4']
    visited = set()
    ans = []
    for i in range(len(s)):
        n_tuple = s[i].split(",") # ['2', '1', '3', '4']
        for num in n_tuple:
            if num in visited:
                continue
            visited.add(num)
            ans.append(int(num))
    return ans
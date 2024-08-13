# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

from collections import defaultdict, deque
def solution(info, edges):
    def dfs(sheep, wolf):
        if sheep<= wolf:
            return

        ans[0] = max(ans[0], sheep)

        for par, child in edges:
            if par in visited and child not in visited:
                visited.add(child)

                if info[child]:
                    dfs(sheep, wolf+1)
                else:
                    dfs(sheep+1, wolf)
                visited.remove(child)

    visited = set()
    visited.add(0)
    ans = [0]
    dfs(1, 0)
    return ans[0]
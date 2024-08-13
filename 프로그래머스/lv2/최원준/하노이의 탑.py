# https://www.acmicpc.net/problem/

'''
1. 아이디어 :
    dfs로 풀 수 있다.
2. 시간복잡도 :
    O(stack)
3. 자료구조 :
    배열
'''


def solution(n):
    '''
    [1,2],[1,3],[2,3]
    [1,3],[1,2],[3,2] , [1,3] , [2,1],[2,3],[1,3]
    [1,2],[1,3],[2,3] , [1,2] , [3,1],[3,2],[1,2] , [1,3] , [2,3],[2,1],[3,1], [2,3], [1,2],[1,3],[2,3]
    '''

    def dfs(start, end, stack):
        mid = 1 if start + end == 5 else 2 if start + end == 4 else 3
        if stack == 2:
            return [[start, mid], [start, end], [mid, end]]

        return dfs(start, mid, stack - 1) + [[start, end]] + dfs(mid, end, stack - 1)

    return dfs(1, 3, n)

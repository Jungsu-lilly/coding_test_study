# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


from collections import defaultdict, deque
def solution(info, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    print(graph)

    cmax = [0]
    sw = [0,0] #sheep, wolve

    sheeps = []

    visited = set()
    visited.add(0)
    def dfs(node, wolves):
        if info[node] == 0:
            sheeps.append(wolves)
            wolves = 0
        else:
            wolves += 1
        for child in graph[node]:
            if child in visited:
                continue
            visited.add(child)
            dfs(child, wolves)

    dfs(0,0)
    print(sheeps)

    sheeps.sort(reverse=True)
    curr = 0
    count = 0
    print(sheeps)
    while curr >= sheeps[-1]:
        count+=1
        curr += sheeps.pop()
    return count

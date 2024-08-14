# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


from collections import defaultdict, deque
def solution(n, roads, sources, destination):
    graph = defaultdict(list)
    for u, v in roads:
        graph[u].append(v)
        graph[v].append(u)
    sources_map = {sources[i]:i for i in range(len(sources))}
    ans = [-1] * len(sources)

    visited = set()
    visited.add(destination)
    queue = deque()
    queue.append((destination, 0))

    while queue:
        curr, time = queue.popleft()
        if curr in sources_map:
            idx = sources_map[curr]
            ans[idx] = time

        for neighbor in graph[curr]:
            if neighbor in visited:
                continue
            visited.add(neighbor)
            queue.append((neighbor, time+1))


    return ans
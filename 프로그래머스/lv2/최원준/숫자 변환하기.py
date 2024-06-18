'''
1. 아이디어 :
    bfs과 memoization으로 풀었습니다
2. 시간복잡도 :
    O( n^3 )
3. 자료구조 :
  해시셋, 덱
'''

from collections import deque
def solution(x, y, n):
    visited = set()
    queue = deque()
    queue.append((x,0))
    
    while queue:
        num, count = queue.popleft()
        if num > y or num in visited:
            continue
        if num == y:
            return count
        visited.add(num)
        queue.append((num+n, count+1))
        queue.append((num*2, count+1))
        queue.append((num*3, count+1))
    
    return -1

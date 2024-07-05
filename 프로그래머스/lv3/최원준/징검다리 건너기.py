'''
1. 아이디어 :
    구간의 최대값들중 최소값이 답
2. 시간복잡도 :
    O( nlogn )
    O( n )
3. 자료구조 :
    힙
    모노토닉 스택
'''

import heapq
def solution(stones, k):

    if len(stones) == k:
        return max(stones)
    ans = []
    max_heap = []

    for i in range(k):
        heapq.heappush(max_heap, (-stones[i],i))
    ans = [-max_heap[0][0]]
    for i in range(k, len(stones)):
        while max_heap and max_heap[0][1] <= i-k:
            heapq.heappop(max_heap)
        heapq.heappush(max_heap, (-stones[i], i))
        ans.append(-max_heap[0][0])
    return min(ans)


from collections import deque
def solution(stones, k):

    if len(stones) == k:
        return max(stones)

    queue = deque()
    ans = []

    for i in range(len(stones)):
        while queue and stones[queue[-1]] <= stones[i]:
            queue.pop()

        queue.append(i)

        if queue[0] <= i-k: #범위에서 벗어날때
            queue.popleft()

        if i >= k-1: #현재 인덱스가 k-1보다 클때
            ans.append(stones[queue[0]])

    return min(ans)
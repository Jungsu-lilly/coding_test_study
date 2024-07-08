'''
1. 아이디어 :
    큐로 구현
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    큐
'''

from collections import deque
def solution(bridge_length, weight, truck_weights):
    total = 0
    count = 0
    arrived = len(truck_weights)
    truck_weights = deque(truck_weights)
    queue = deque([0] * bridge_length)

    while arrived:
        if queue[0] != 0:
            arrived -= 1
        total -= queue.popleft()

        if truck_weights and total + truck_weights[0] <= weight:
            total += truck_weights[0]
            queue.append(truck_weights.popleft())
        else:
            queue.append(0)

        count += 1
    return count

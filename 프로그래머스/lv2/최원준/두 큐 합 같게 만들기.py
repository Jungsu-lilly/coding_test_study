'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''

from collections import deque
def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    total1 = sum(queue1)
    target = (total1+sum(queue2))//2

    count = 0
    for i in range(len(queue1)*3):
        if total1 == target:
            return count
        elif total1 > target:
            val = queue1.popleft()
            total1 -= val
            queue2.append(val)
            count+=1
        elif total1 < target:
            val = queue2.popleft()
            total1 += val
            queue1.append(val)
            count+=1

    return -1
'''
1. 아이디어 :
    큐를 사용해서 마지막 버스까지 태워보낸다
    마지막 버스시간 이거나  마지막 인원의 시간보다 1분 앞이 정답
2. 시간복잡도 :
    O( n * m )
3. 자료구조 :
    큐
'''

from collections import deque
def solution(n, t, m, timetable):

    def convert(s): #시간을 값으로 변환
        left, right = map(int, s.split(":"))
        return left * 60 + right

    def convert_n(n): #값을 시간으로 변환
        hour = str(n // 60)
        if len(hour) == 1:
            hour = "0" + hour
        min = str(n % 60)
        if len(min) == 1:
            min = "0" + min
        return hour + ":" + min


    timetable.sort()
    bus = [9*60 + t * i for i in range(n)] # 버스 도착 시간
    queue = deque() #큐에 크루들 줄서는 시간 저장
    for s in timetable:
        queue.append(convert(s))

    for i in range(len(bus)-1): #버스가 1대 남을때까지 큐에서 m만큼 뺀다.
        bus_arrive = bus[i]
        for j in range(m):
            if queue and queue[0] <= bus_arrive:
                queue.popleft()

    if len(queue) >= m:
        return convert_n(min(queue[m-1]-1, bus[-1]))
    else:
        return convert_n(bus[-1])
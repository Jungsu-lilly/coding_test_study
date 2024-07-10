'''
1. 아이디어 :
    큐를 사용해서 마지막 버스까지 태워보낸다
    한자리를 제외하고 탈 수 있는 나머지 사람들을 태운다.
    더 이상 탈 사람이 없으면, 버스가 도착한 시간에 타면되고,
    줄을 기다리고 있으면, 마지막 자리에 탈 사람보다 1분 일찍 줄을 서면 된다
2. 시간복잡도 :
    O( n * m )
3. 자료구조 :
    큐
'''

from collections import deque


def solution(n, t, m, timetable):
    def serialize(time):
        hour, minite = time.split(":")
        return int(hour) * 60 + int(minite)

    def deserialize(n):
        hour, minite = str(n // 60), str(n % 60)
        hour = "0" + hour if len(hour) == 1 else hour
        minite = "0" + minite if len(minite) == 1 else minite
        return hour + ":" + minite

    timetable = deque(sorted(timetable))
    bus = deque([540 + (t * i) for i in range(n)])

    while len(bus) > 1:
        time = bus.popleft()
        for i in range(m):
            if timetable and serialize(timetable[0]) <= time:
                timetable.popleft()

    for i in range(m - 1):
        if timetable and serialize(timetable[0]) < bus[0]:
            timetable.popleft()

    if not timetable:
        return deserialize(bus[0])
    else:
        return deserialize(min(bus[0], serialize(timetable[0]) - 1))
    return ""

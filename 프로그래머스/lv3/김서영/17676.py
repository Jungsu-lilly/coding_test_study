"""
추석 트래픽
https://school.programmers.co.kr/learn/courses/30/lessons/17676
"""


from collections import defaultdict
def solution(lines):
    def serialize(time):
        date, time, dur = time.split()
        h, m, s = time.split(":")
        s, ms = s.split(".")
        dur = int(float(dur[:-1]) * 1000)
        end = int(h) * 3600 * 1000 + int(m) * 60 * 1000 + int(s) * 1000 + int(ms)
        return [end - dur + 1, end]

    logs = []
    for line in lines:
        start, end = serialize(line)
        logs.append((start, "s"))
        logs.append((end + 1000, "e"))
    logs.sort()

    ans = count = 0
    for log in logs:
        if log[1] == "s":
            count += 1
            ans = max(ans, count)
        else:
            count -= 1
    return ans

def solution_tmp(lines):
    """
    lines = "S T"
    S = 2016-09-15 hh:mm:ss.sss = 응답 완료시간
    T = 소수점_셋째_s = 처리시간
    """
    import math
    # float으로 처리를 하는게 낫겟다
    def to_sec(s, t):
        hr, m, sec = map(float, s.split(':'))
        end = hr*3600 + m*60 + sec
        processed_t = float(t[:-1])    
        return end-processed_t+0.001, end
    
    timeline = []
    for line in lines:
        _, s, t = line.split()
        start, end = to_sec(s, t)
        timeline += [(start, 's'), (end, 'e')]
    timeline.sort(key=lambda x: (x[0], x[1][::-1]))
    print(timeline)
    
    n = len(timeline)
    answer = 0
    # 모든 포인트를 시작점으로 1초 구간 내에 s인 거 개수 구해보면서 최대값 업데이트
    for i, t in enumerate(timeline):
        j, thoughput = i+1, 1 # incremental idx, 1초 구간 내 처리 수
        while j < n and timeline[j][0] <= t[0]+1.0:
            if timeline[j][1] == 's': thoughput+=1
            j+=1
        answer = max(answer, thoughput)

    return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/42576

from collections import Counter

def solution(participant, completion):
    answer = ''
    participant_count = Counter(participant)
    completion_count = Counter(completion)
    for i in participant_count:
        if completion_count[i]:
            participant_count[i] -= completion_count[i]
    for i in participant_count:
        if participant_count[i] > 0:
            answer += i # 만약 mislav가 3명 있는데 한명만 완주하면? answer += i*participant_count[i]
    return answer

solution(["leo", "kiki", "eden"], ["eden", "kiki"])
# solution(["marina", "josipa", "nikola", "vinko", "filipa"],	["josipa", "filipa", "marina", "nikola"])
# solution(["mislav", "stanko", "mislav", "ana"],	["stanko", "ana", "mislav"])

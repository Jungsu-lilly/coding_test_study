
'''
1. 아이디어 :
    누적합을 통해서 시간 단축
    0~5, 3~9
    [1,  0,  0,  1,  0, -1,  0,  0,  0,  0, -1]
    [1,  1,  1,  2,  2,  1,  1 , 1 , 1,  1,  0]
    [1,  2,  3,  5,  7,  8,  9, 10, 11, 12, 12]
    3~8 = [2,  2,  1,  1 , 1 , 1] = 8
    8-2 = 11 - 3 = 8
2. 시간복잡도 :
    O( play_time )
3. 자료구조 :
    배열
'''


def solution(play_time, adv_time, logs):
    def serialize(time):
        h, m, s = time.split(":")
        return int(h) * 3600 + int(m) * 60 + int(s)

    def deserialize(num):
        h = str(num // 3600)
        if len(h) == 1:
            h = "0" + h
        num = num % 3600
        m = str(num // 60)
        if len(m) == 1:
            m = "0" + m
        num = num % 60
        s = str(num)
        if len(s) == 1:
            s = "0" + s
        return h + ":" + m + ":" + s

    play_time = serialize(play_time)
    adv_time = serialize(adv_time)

    counter = [0] * (play_time + 1)
    for log in logs:
        start, end = log.split("-")
        start, end = serialize(start), serialize(end)
        counter[start] += 1
        if end < play_time:
            counter[end] -= 1

    #특정 시간의 시청자 수
    for i in range(1, play_time + 1):
        counter[i] += counter[i - 1]

    #범위의 시청자 수를 구하기 위한 누적합
    for i in range(1, play_time + 1):
        counter[i] += counter[i - 1]

    ans_score = 0
    ans_time = 0

    for start in range(play_time - adv_time + 1):
        end = start + adv_time
        if start == 0:
            current_view_time = counter[end - 1]
        else:
            current_view_time = counter[end - 1] - counter[start - 1]

        if current_view_time > ans_score:
            ans_score = current_view_time
            ans_time = start

    return deserialize(ans_time)




# https://www.acmicpc.net/problem/

'''
1. 아이디어 :
    정렬
2. 시간복잡도 :
    O( nlog n)
3. 자료구조 :
    배열
'''


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

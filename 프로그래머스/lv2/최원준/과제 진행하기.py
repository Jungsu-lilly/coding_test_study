# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


def solution(plans):
    def serialize(s):
        hour, minite = s.split(":")
        return int(hour) * 60 + int(minite)

    plans = sorted([(name, serialize(start), int(dur)) for name, start, dur in plans], key=lambda x:x[1])
    name, start, dur = plans[0]
    # print(plans)
    # print()
    ans = []
    curr = start
    stack = [(name, dur)]

    for name, start, dur in plans[1:]:
        while stack and curr < start:
            cname, cdur = stack.pop()
            if curr + cdur <= start: #현재시간 + 지속시간 <= 다음 시작시간:
                ans.append(cname)
                curr += cdur
            else: #남은 시간 저장:
                stack.append((cname, cdur - (start - curr)))
                break
            # print(stack, curr)

        stack.append((name, dur))
        curr = start
        # print(stack, curr)
    while stack:
        ans.append(stack.pop()[0])
    return ans

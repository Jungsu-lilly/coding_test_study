'''
1. 아이디어 :
    -
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    배열
'''

from collections import defaultdict
def solution(record):

    def print_message(behave, uid):
        suffix = "님이 들어왔습니다." if behave == "Enter" else "님이 나갔습니다."
        return uid_mapper[uid] + suffix

    uid_mapper = defaultdict(str)
    for i in range(len(record)):
        record[i] = record[i].split()

    for r in record:
        if len(r) == 3:
            uid_mapper[r[1]] = r[2]

    ans = []
    for r in record:
        if r[0] != "Change":
            ans.append(print_message(r[0], r[1]))

    return ans
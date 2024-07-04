'''
1. 아이디어 :
    bid와 uid가 같은지 확인한다
    해시맵에 넣고, 백트래킹으로 조합들을 구한다
2. 시간복잡도 :
    O( ?? )
3. 자료구조 :
    해시셋, 해시맵, 배열
'''

from collections import defaultdict
def solution(user_id, banned_id):

    def check(banned_id, user_id):
        if len(banned_id) != len(user_id):
            return False
        for i in range(len(banned_id)):
            if banned_id[i] == "*":
                continue
            if banned_id[i] != user_id[i]:
                return False
        return True

    def backtrack(idx, arr):
        if idx == len(banned_id):
            combins.add(",".join(sorted(arr)))
            return

        for c in candid[idx]:
            if c not in arr:
                backtrack(idx+1, arr + [c])

    candid = defaultdict(list)
    for i, bid in enumerate(banned_id):
        for uid in user_id:
            if check(bid, uid):
                candid[i].append(uid)

    combins = set()
    backtrack(0, [])

    return len(combins)
from itertools import product
# banned_id를 돌면서 user_id를 하나씩 체크(완전탐색)
# 해당하는 아이디의 경우의 수 체크해서 조합 생성
# 중복된 아이디가 있거나 이미 체크한 경우라면 제외

# 5번 테케 시간초과 남

def findBlind(s):
    cnt = []
    for i in range(len(s)):
        if s[i] == '*':
            cnt.append(i)
    return cnt

def changeToBlind(s,blind):
    s = list(s)
    for i in blind:
        s[i] = '*'
    return s

def solution(user_id, banned_id):
    combi = [[] for i in range(len(banned_id))]
    
    for idx,ban in enumerate(banned_id):
        blind = findBlind(ban)
        for user in user_id:
            if len(user) == len(ban):
                changedUser = changeToBlind(user,blind)
                if changedUser == list(ban) :
                    combi[idx].append(user)
                    
    cartesian = (list(product(*combi)))
    answer = []
    
    for i in cartesian:
        # 하나의 조합 내에 있는 중복 제거
        i = set(list(i))
        if len(i) == len(banned_id):
            answer.append(tuple(sorted(i)))
    # answer를 set으로 변환하여 조합 중복 제거
    answer = set(answer)
    
    return len(answer)
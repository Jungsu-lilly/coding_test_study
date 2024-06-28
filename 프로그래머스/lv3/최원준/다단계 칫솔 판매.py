'''
1. 아이디어 :
    dfs를 사용해서 풀 수 있다
2. 시간복잡도 :
    O( n^2 )
3. 자료구조 :
    해시맵
'''

from collections import defaultdict
import math

def solution(enroll, referral, seller, amount):
    def dfs(name, income):
        if name == "-" or income == 0:
            return
        commission = math.floor(income * 0.1)
        profit[name] += income - commission
        dfs(par[name], commission)

    par = {enroll[i] : referral[i] for i in range(len(enroll))}
    profit = defaultdict(int)

    for i in range(len(seller)):
        dfs(seller[i], amount[i] * 100)

    return [profit[person] for person in enroll]
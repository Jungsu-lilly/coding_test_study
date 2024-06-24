'''
1. 아이디어 :
    Win_against 트래킹하는 해시맵, Lost_against 트래킹하는 해시맵 두개를 만든다
    A가 B를 이기고, B가 C를 이겼을때, C는 A한테 졌으므로 Lost_against[c]에 B가 졌던 A를 추가한다.
    이긴사람+진사람 == n -1을 카운트

    # A가 B를 이기고, B가 C를 이겼을때, A가 C도 이겼다고 업데이트 할시에,
    ## for loop이 동작하는 동안 A의 Win_aginst 값이 업데이트가 되어서 오류
2. 시간복잡도 :
    O( n^3 ) for player * for loser * update
3. 자료구조 :
    해시맵
'''

from collections import defaultdict

def solution(n, results):
    win_against = defaultdict(set)
    lost_against = defaultdict(set)
    for winner, loser in results:
        win_against[winner].add(loser)
        lost_against[loser].add(winner)

    for player in range(1, n+1):
        for loser in win_against[player]:
            lost_against[loser].update(lost_against[player])
        for winner in lost_against[player]:
            win_against[winner].update(win_against[player])

    return sum([1 for i in range(1+n) if len(win_against[i]) + len(lost_against[i]) == n-1])




"""
외벽 점검
https://school.programmers.co.kr/learn/courses/30/lessons/60062

완전탐색
전체 경우의 수가 뭔지 생각해보기가 첫번째.
a. 각 dist 순서에서 점검 어디까지 할 수 있는지 체크, 즉 dist의 모든 permuation
    [3, 5, 7] -> (3, 5, 7)(3, 7, 5)(5, 3, 7)(5, 7, 3)(7, 3, 5)(7, 5, 3)
b. 각 permutation 에서 차례차례 취약점 [1, 3, 4, 9, 10] 검사해서 minCnt 업데이트
    startpoint 위치 잡는것도 모든 경우의 수 다 고려해야함.
    (3, 5, 7)에서 3체크할 수 있는 애가 1부터 시작 -> 3부터 시작 -> 4부터 시작 -> ... 했을때
"""

def solution(n, weak, dist):
    from itertools import permutations

    n_weak = len(weak)
    # 반시계 방향까지 고려하지 않고 한 방향으로만 생각하기 위해 원 펴기
    weak += [w+n for w in weak]
    answer = 1e10

    # 가능한 모든 시작 지점 - 취약점 위치들
    for startpoint in range(len(n_weak)):
         # 가능한 모든 점검 순서(점검 종류) - dist 순열
         for p in permutations(dist, len(dist)):
            # 모든 취약점 방문 될 때까지 친구 한명씩 써보기
            cnt, pos = 1, startpoint                # 사용한 친구 수, 점검 취약점 position
            for i in range(1, len(n_weak)):
                nextpos = startpoint + i            # startpoint 다음 취약점까지의 거리를 보고
                diff = weak[nextpos] - weak[pos]
                if diff > p[cnt-1]:                 # 현재 점검할 대상 후보가 점검할 수 있는 거리보다 크면 친구 늘리기
                    pos = nextpos
                    cnt += 1
                if cnt > len(dist): break           # 친구 다 썼으면 invalid case
            
            if cnt <= len(dist):answer = min(answer, cnt) # 한번 점검 순서 x 케이스 다 돌았으니 이때의 min값이 유의미한지 체크

    return answer


# solution(12, [1, 5, 6, 10], [1, 2, 3, 4])
solution(12, [1, 3, 4, 9, 10], [3, 5, 7])
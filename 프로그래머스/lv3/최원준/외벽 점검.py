# https://www.acmicpc.net/problem/

'''
1. 아이디어 :
    원형을 선형으로 바꾼다.
    투입되는 사람들의 모든 조합을 확인한다.
    해당 조합에서,
        weak의 시작점마다,
            weak의 시작점에서 해당조합의 첫번째 사람이 도달할 수 있는 거리를 구한다.
            도달할 수 있는 거리가 다음 weak의 지점보다 작을시,
                다음 사람이 도달할 수 있는 거리를 구한다.
2. 시간복잡도 :
    O( dist! * weak**2)
3. 자료구조 :
    배열
'''



from itertools import permutations
def solution(n, weak, dist):
    size = len(weak)
    for i in range(size-1):
        weak.append(weak[i] + n)
    # print(weak)
    ans = len(dist) + 1

    for comb in permutations(dist): #모든 조합
        for start in range(size): # weak의 시작점
            count = 1

            # 사람이 weak의 시작지점(start)에서 조합에서 처음 사람이 갈 수 있는 거리
            pos = weak[start] + comb[count-1]

            for i in range(start, start+size): #시작 지점부터 도착 지점
                if pos < weak[i]:
                    count += 1
                    if count > len(comb):
                        break
                    pos = weak[i] + comb[count-1]
            ans = min(ans, count)

    return -1 if ans > len(dist) else ans


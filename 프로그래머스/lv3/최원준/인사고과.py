#

'''
1. 아이디어 :
    내림차순, 오름차순 정렬한다.
2. 시간복잡도 :
    O(nlogn)
3. 자료구조 :
    배열
'''

def solution(scores):
    target = scores[0]
    target_sum = sum(target)
    scores.sort(key=lambda x: (-x[0], x[1])) #정렬을 통해, 항상 뒤에 있는
    # 	[[3, 2], [3, 2], [2, 1], [2, 2], [1, 4]]

    cmax = 0
    ans = 1
    for score in scores:
        if target[0] < score[0] and target[1] < score[1]:
            return -1
        if cmax <= score[1]: #cmax보다 작으면
            if target_sum < score[0] + score[1]:
                ans += 1
            cmax = score[1]
            #항상 1번째 값은 최대값으로 한다.
            #뒤에 오는 값들은 0번의 값으로 정렬되어있으므로,
            #cmax보다 크거나 같다면, 지워지지 않는 거고,
            #지워지지 않으면 target_sum과 비교해서 랭크를 하나씩 밀어낸다.
    return ans

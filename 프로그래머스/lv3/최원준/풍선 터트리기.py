# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


def solution(a):
    n = len(a)
    if n == 1:
        return 1

    left_min = [0] * n
    left_min[0] = a[0]

    right_min = [0] * n
    right_min[n - 1] = a[n - 1]

    # 왼쪽 최소값 계산
    for i in range(1, n):
        left_min[i] = min(left_min[i - 1], a[i])

    # 오른쪽 최소값 계산
    for i in range(n - 2, -1, -1):
        right_min[i] = min(right_min[i + 1], a[i])

    print(left_min)
    print(right_min)

    answer = 0
    for i in range(n):
        if a[i] <= left_min[i] or a[i] <= right_min[i]:
            answer += 1

    return answer




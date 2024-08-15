# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

def solution(a):
    n = len(a)

    left_min = [a[0]] * n
    right_min = [a[n-1]] * n

    # 왼쪽 최소값 계산
    for i in range(1, n):
        left_min[i] = min(left_min[i - 1], a[i])

    # 오른쪽 최소값 계산
    for i in range(n - 2, -1, -1):
        right_min[i] = min(right_min[i + 1], a[i])

    return len(a) - sum([1 for i in range(n) if right_min[i] < a[i] > left_min[i]])




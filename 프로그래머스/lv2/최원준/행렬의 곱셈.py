# https://www.acmicpc.net/problem/

'''
1. 아이디어 :
    arr1의 row * arr2의 col 배열을 초기화한다.
    arr1의 col(또는 arr2의 row)만큼 순회를 하면서 arr1, arr2의 곱한 값을 ans에 더한다.
2. 시간복잡도 :
    O(n * m * k)
3. 자료구조 :
    배열
'''


def solution(arr1, arr2):
    r = len(arr1)
    c = len(arr2[0])
    ans = [[0 for _ in range(c)] for _ in range(r)]

    for row in range(r):
        for col in range(c):
            for i in range(len(arr1[0])):
                ans[row][col] += arr1[row][i] * arr2[i][col]
    return ans

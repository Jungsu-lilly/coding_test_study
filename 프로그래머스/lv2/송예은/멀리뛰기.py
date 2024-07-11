# 접근 - DP
# n의 방법 가짓수는 (n-1의 방법 + n-2의 방법) 가짓수와 같음

def solution(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    arr = [0]*(n+1)
    arr[1] = 1
    arr[2] = 2
    for i in range(3,n+1):
        arr[i] = arr[i-1]+arr[i-2]

    return arr[n] % 1234567
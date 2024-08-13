"""
3*n 타일링
https://school.programmers.co.kr/learn/courses/30/lessons/12902?language=python3

n이 홀수인 경우 완전한 타일링을 할 수 없어도 타일이 놓아질 수 있는 경우의 수를 만들어놓고
다음 타일링에서 이걸 base로 배치할 수 있는 경우의 수를 고려한다.
- 모양 과 | 모양 이 있다.

n=1 : | 모양을 위쪽에 배치 & 아래에 배치 -> 2가지 케이스
n=2 : 3가지 케이스
n=3 : `n=2 케이스`들에서 `각각 | 모양을 위쪽에 배치 & 아래에 배치(*2)` + 
        `n=1 케이스` 에서 가능한 타일 붙히기
n=4 : `n=2 케이스`들에서 가로 2짜리 완전하게 타일링 이어서 붙히기 + 
        `n=3 케이스`들에서 완전하게 타일링 만들기
"""

def solution(n):
    print(f"\nsolution {n}")
    dp = [0] * (n+1)
    dp[1] = 2
    dp[2] = 3
    
    for i in range(3,n+1):
        if i % 2 == 0:
            dp[i] = dp[i-1] + dp[i-2]
        else:
            dp[i] = dp[i-1]*2 + dp[i-2]
        print(dp)
    return dp[n]%1000000007


solution(4)
solution(6)
solution(8)
solution(10)
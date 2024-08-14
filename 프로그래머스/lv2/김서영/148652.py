""" 1-> 11011 0-> 00000
C(0)  1   
C(1)  11011  
C(2)  11011 11011 00000 11011 11011 
C(3)  11011 11011 00000 11011 11011  11011 11011 00000 11011 11011  00000 00000 00000 00000 00000  11011 11011 00000 11011 11011  11011 11011 00000 11011 11011

      len     numof_1
C(1)   5        4
C(2)   25       16
C(3)   125      64
...
C(20)  5^20     4^20

5개의 토막 0/1/2/3/4 로 나누고 각 구역에서 재귀호출

- 재귀 정의
recursion(n, k) = C(n)의 k번째 수까지 1 개수
그럼 recursion(n, r) - recursion(n, l-1) 리턴

- 재귀 구현
f = (k가 위치한 토막-1까지 1 개수) + f(n-1, k-(토막 전까지의 비트수))
"""

def solution(n, l, r):
    def recursion(n, k):
        if n == 1: return k if k<=2 else k-1

        div = 5**(n - 1)
        numof_1 = 4**(n - 1)
        partition = k // div

        if k % div == 0: partition -= 1

        if partition < 2: 
            return numof_1 * partition + recursion(n - 1, k - partition * div)
        elif partition == 2:
            return numof_1 * partition
        else:
            return numof_1 * (partition - 1) + recursion(n - 1, k - partition * div)
    
    return recursion(n, r) - recursion(n, l-1)



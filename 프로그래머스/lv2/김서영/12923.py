"""
숫자 블록
https://school.programmers.co.kr/learn/courses/30/lessons/12923

자기 자신이 아닌 약수 구하기
"""


def solution(begin, end):

    def get_max_measure_1(n):
        if n==1: return 0
        for i in range(n//2, 0, -1):
            if n%i == 0 and i<=10000000: return i
        
    def get_max_measure_2(n):
        if n==1: return 0
        max_limit = min(10000000, n//2)
        for i in range(max_limit, 0, -1):
            if n%i==0: return i
        
    def get_max_measure_3(n):
        pass
            
    answer = []
    for i in range(begin, end + 1):        
        x = get_max_measure_2(i)
        # print(f"  i:{i} x:{x}")
        answer.append(x)
    return answer
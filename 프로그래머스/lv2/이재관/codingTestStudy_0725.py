
def solution(n):
    answer = ''
    rule = ['1', '2', '4']

    while n > 0:
        n -= 1
        d = n % 3
        n = n // 3
        answer = rule[d] + answer

    return answer
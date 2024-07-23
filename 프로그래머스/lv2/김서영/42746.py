"""
가장 큰 수
https://school.programmers.co.kr/learn/courses/30/lessons/42746
"""

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return '0' if numbers[0]=='0' else ''.join(numbers)


solution([6, 10, 2])
# 6 2 10
solution([3, 30, 34, 5, 9])
# 9 5 34 3 30
solution([0, 0])
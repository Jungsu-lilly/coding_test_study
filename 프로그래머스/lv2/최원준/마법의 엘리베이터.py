# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


def solution(storey):
    count = 0

    while storey:
        remainder = storey % 10
        if remainder > 5:
            count += (10 - remainder)
            storey += 10
        elif remainder < 5:
            count += remainder

        elif remainder == 5:
            if (storey // 10) % 10 > 4:
                storey += 10
            count += remainder
        storey = storey // 10

    return count
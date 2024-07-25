# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


def solution(n):
    def convert(n):
        nums = []
        while n > 0:
            n -= 1  # 값을 1 줄여서 0, 1, 2가 아닌 1, 2, 3이 되도록 조정
            nums.append(n % 3 + 1)
            n //= 3
        return nums[::-1]

    map = {1:"1", 2:"2", 3:"4"}
    arr = convert(n)
    return "".join([map[arr[i]] for i in range(len(arr))])
# https://www.acmicpc.net/problem/

'''
1. 아이디어 :
    투 포인터로 풀 수 있습니다.
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    해시맵, 배열
'''


def solution(msg):
    dict = {chr(i + 64): i for i in range(1, 27)}
    next = 27

    ans = []
    start = 0
    end = start + 1

    while start < len(msg):
        temp = msg[start]
        while end < len(msg) and temp + msg[end] in dict:
            temp += msg[end]
            end += 1
        ans.append(dict[temp])
        if end < len(msg):
            dict[temp + msg[end]] = next
            next += 1

        start = end
        end += 1
    return ans

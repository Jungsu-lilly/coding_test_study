# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


import sys
#sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def solution(data, col, row_begin, row_end):
    # print(*data, sep='\n')
    data.sort(key=lambda x: (x[col-1], -x[0]))
    values = []
    for i in range(row_begin-1, row_end):
        temp = 0
        for row_value in data[i]:
            temp += row_value%(i+1)
        values.append(temp)
    ans = values[0]
    for v in values[1:]:
        ans = ans ^ v
    return ans
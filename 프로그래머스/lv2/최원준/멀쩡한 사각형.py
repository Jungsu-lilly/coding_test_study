# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


import math
def solution(w,h):
    def gcd(a,b):
        if b==0:
            return a
        else:
            return gcd(b,a%b)

    ans = w*h
    scale = gcd(w,h)
    ans -= ((w//scale + h//scale) - 1 ) * scale
    return ans



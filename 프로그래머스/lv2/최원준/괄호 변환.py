# https://www.acmicpc.net/problem/

'''
1. 아이디어 :
    dfs 구현
2. 시간복잡도 :
    O( n**2 )
3. 자료구조 :
    스택
'''


import sys
#sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def solution():

    return 1

def solution(p):
    def check(s):
        stack = []
        for c in s:
            if c == "(":
                stack.append(c)
            elif c == ")":
                if not stack:
                    return False
                stack.pop()
        return False if stack else True

    def get_idx(s):
        count = 0
        for i, c in enumerate(s):
            if c == "(":
                count += 1
            elif c == ")":
                count -= 1
            if count == 0:
                return i + 1

    def reverse(s):
        a = ""
        for c in s:
            if c == "(":
                a += ")"
            else:
                a += "("
        return a

    def dfs(s):
        if s == "":
            return ""
        idx = get_idx(s)
        u = s[:idx]
        v = s[idx:]

        if check(u):
            return u + dfs(v)
        else:
            temp = "("
            temp += dfs(v)
            temp += ")"
            temp += reverse(u[1:-1])
            return temp

    return dfs(p)


print(solution())



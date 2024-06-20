#

'''
1. 아이디어 :
    Monotonic Stack 사용
2. 시간복잡도 :
    O ( n )
3. 자료구조 :
    배열
'''

def solution(numbers):
    stack = []
    ans = [-1] * len(numbers)
    for i, n in enumerate(numbers):
        while stack and stack[-1][0] < n:
            val, idx = stack.pop()
            ans[idx] = n
        stack.append((n,i))
    return ans
# s를 0부터 s의 길이-1까지 회전시키면서 확인

opens = ['(','{','[']

def isValid(s):
    stack = []
    for i in s:
        if i in opens:
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
        elif i == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(i)
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
    if not stack :
        return True
    return False

def solution(s):
    ans = 0
    if isValid(s) :
        ans += 1
    for i in range(1,len(s)):
        s = s[1:] + s[0]
        if isValid(s):
            ans += 1
    return ans
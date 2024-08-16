# https://www.acmicpc.net/problem/

'''
1. 아이디어 :
    0 뒤에 또는 11 앞에 "110"을 넣는다
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    스택
'''

def solution(s):
    ans = []

    for string in s:
        count_110 = 0
        stack = []

        for char in string:
            stack.append(char)
            if len(stack) >= 3 and stack[-3:] == ['1', '1', '0']:
                count_110 += 1
                for _ in range(3):
                    stack.pop()
        string = "".join(stack)

        index = len(string)
        found = False
        #마지막 0 뒤
        for i in range(len(string) - 1, -1, -1):
            if string[i] == '0':
                index = i + 1
                found = True
                break
        #첫 11 앞
        if not found:
            for i in range(len(string)):
                if string[i] == '1':
                    index = i
                    break

        string = string[:index] + ("110" * count_110) + string[index:]
        ans.append(string)

    return ans

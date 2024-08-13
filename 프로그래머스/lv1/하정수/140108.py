def solution(s):
    ans = 0
    a, b = 0, 0
    k = ''
    
    for i in s:
        if a == b:
            k = i
            ans += 1
            a, b = 0, 0
        if k == i:
            a += 1
        else:
            b += 1
            
    return ans

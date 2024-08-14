def solution(s, skip, index):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    ans = ""
    
    for i in skip:
        alpha = alpha.replace(i,"")
        
    for a in s:
        ans += alpha[(alpha.find(a) + index) % len(alpha)]
    return ans

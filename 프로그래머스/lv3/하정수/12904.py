def solution(s):
    ans = 1
    n = len(s)
    
    for i in range(n):
        기준 = s[i]        
        l, r = i-1, i+1
        tmp = 1

        while l>=0 and r<n:
            if s[l] == s[r]: 
                tmp += 2
                l,r = l-1, r+1
                continue
            break
        
        ans = max(ans, tmp)
        
    for i in range(n-1):
        if s[i] != s[i+1]: continue
        l, r = i-1, i+2
        tmp = 2
        
        while l>=0 and r<n:            
            if s[l] == s[r]:
                tmp += 2
                l,r = l-1, r+1
                continue
            break    
        ans = max(ans, tmp)
        
    return ans

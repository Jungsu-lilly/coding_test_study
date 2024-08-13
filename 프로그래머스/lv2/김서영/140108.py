# 첫 글자 x
# x와 x가 아닌 다른 글자들이 나온 횟수를 각각 셉니다. 
# 처음으로 두 횟수가 같아지는 순간 멈추고, 지금까지 읽은 문자열을 분리
"""
banana -  ba - na - na
abracadabra - ab - ra - ca - da - br - a
aaabbaccccabba - aaabbacc - ccab - ba
"""
def solution(s):
    answer = 0
    i = 0
    while i < len(s):
        x = s[i]
        n_x, n_diff = 0, 0
        
        for j in range(i, len(s)):
            if s[j] == x: n_x += 1
            else: n_diff += 1
            
            if n_x == n_diff: break
                
        answer += 1
        i = j + 1
    return answer

solution("banana")
solution("aaabbaccccabba")
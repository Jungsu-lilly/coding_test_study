""" lv2. 튜플
"""

def solution(s):    
    import re
    
    # left_b number, right_b.  \{   \d, +  \}
    elements = re.findall(r'\{[\d,]+\}', s) #['{2}', '{2,1}', '{2,1,3}', '{2,1,3,4}']
    elements.sort(key=len)
    
    answer = []
    for e in elements:
        set_ = set(e[1:-1].split(','))
        x = list(set_ - set(answer))
        answer.append(x[0])
    
    return list(map(int, answer))
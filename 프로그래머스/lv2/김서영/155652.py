def solution(s, skip, index):
    alp = ''
    for a in 'abcdefghijklmnopqrstuvwxyz':
        if a not in skip: alp += a
        
    answer = ''
    for e in s:
        e_loc = alp.find(e)
        answer += alp[(e_loc+index)%len(alp)]
    return answer
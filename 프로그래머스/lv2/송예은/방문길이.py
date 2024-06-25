# seen을 체크하면서 이동

maps = {'U':0,'D':1,'R':2,'L':3}

def solution(dirs):
    seen = []
    curr = [0,0]
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    for i in dirs:
        
        ny = curr[0] + dy[maps[i]]
        nx = curr[1] + dx[maps[i]]
        load = [(curr[0],curr[1]),(ny,nx)]
        switchLoad = [(ny,nx),(curr[0],curr[1])]
        
        if ny < -5 or nx < -5 or ny > 5 or nx > 5 :
            continue
        curr = [ny,nx]
        
        if load in seen or switchLoad in seen:
            continue
        seen.append(load)
        
    return (len(seen))
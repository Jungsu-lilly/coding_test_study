def solution(line): # Ax + By + C = 0
    n = len(line)
    ans = []
    result = []
    
    for i in range(n):
        for j in range(i+1, n):
            l1 , l2 = line[i], line[j]
            A, B, E = l1
            C, D, F = l2
            if A*D - B*C == 0:
                continue
            if (B*F-E*D)%(A*D-B*C) == 0 and (E*C-A*F)%(A*D-B*C) == 0:
                x = int( (B*F-E*D)/(A*D-B*C) )
                y = int( (E*C-A*F)/(A*D-B*C) )
                ans.append([x,y])
    
    ans.sort(key = lambda x: (-x[1], x[0]))  # y좌표 내림차순, x좌표 오름차순
    mx, Mx, my, My = float('inf'), -float('inf'), float('inf'), -float('inf')
    
    for l in ans:
        mx = min(mx, l[0])
        Mx = max(Mx, l[0])
        my = min(my, l[1])
        My = max(My, l[1])
    len_y = My-my + 1
    len_x = Mx-mx + 1
    idx = 0
    
    for y in range(My, my-1, -1):
        tmp = ['.'] * len_x
        while idx < len(ans) and ans[idx][1] == y:
            tmp[ans[idx][0]-mx] = '*'
            idx += 1
        str = ''
        for i in tmp:
            str += i
        result.append(str)
            
    return result

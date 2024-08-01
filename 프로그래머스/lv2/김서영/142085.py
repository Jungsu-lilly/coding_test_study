def solution(n, k, enemy):
    import heapq
    
    if len(enemy)==k: return k

    idx_enemy = [(-e, i) for i, e in enumerate(enemy)]
    heapq.heapify(idx_enemy)

    total = sum(enemy)
    # for i in range(len(enemy)-1, -1, -1):
        # if n >= sum(sorted(enemy[:i+1], reverse=True)[k:]): return i+1
    for i in range(len(enemy)):
        if i not in (x[1] for x in idx_enemy[:k]):
            s = sum(x[0] for x in idx_enemy[k:]) * (-1)
            if n >= total-s: return i+1
            print(total, s)
            
            
        total-=enemy[i]
        
    return -1
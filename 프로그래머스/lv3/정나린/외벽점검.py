def solution(n, weak, dist):
    dist.sort(reverse=True)
    repaired = [()]
    count = 0
    
    for d in dist:
        count += 1
        can_reach_arr = []
        for i, v in enumerate(weak):
            start = v
            ends = weak[i:] + [n + w for w in weak[:i]]
            can_reach = [end % n for end in ends if end - start <= d] 
            can_reach_arr.append(set(can_reach))
        
        candidate = set()
        for can_reach_set in can_reach_arr:
            for r in repaired:
                new_set = can_reach_set | set(r)
                if len(new_set) == len(weak):
                    return count
                candidate.add(tuple(new_set))
        repaired = candidate
            
    return -1

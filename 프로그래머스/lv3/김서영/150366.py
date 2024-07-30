def solution(commands):
    from collections import defaultdict
    
    # table : {(i,j): [val, [merged_status]]}
    #       - merge_status : (i, j)와 병합되어있는 좌표값들
    table = defaultdict(lambda: ['', set()]) 
    answer = []
    
    def update1(r, c, value):
        # (r, c) 위치에 value 추가 or 갱신
        table[(r, c)][0] = value
        for (i, j) in table[(r, c)][1]:
            table[(i, j)][0] = value
        
    def update2(value1, value2):
        # val1 전부 val2로 바꾸기
        for key, val in table.items():
            if val[0]==value1: 
                table[key][0] = value2
                for (i, j) in val[1]: 
                    table[(i, j)][0] = value2
                
    def merge(r1, c1, r2, c2):
        if r1==r2 and c1==c2: return 
        cell1_has_val = (r1, c1) in table.keys()
        cell2_has_val = (r2, c2) in table.keys()
        cell1_had_merged = cell1_has_val and table[(r1, c1)][1]
        cell2_had_merged = cell2_has_val and table[(r2, c2)][1]

        if not cell1_has_val and cell2_has_val:
            val = table[(r2, c2)][0]
        else:
            val = table[(r1, c1)][0]

        table[(r1, c1)][1].add((r2, c2))
        table[(r2, c2)][1].add((r1, c1))
        if cell1_had_merged and cell2_had_merged:
            table[(r1, c1)][1].update(table[(r2, c2)][1])
            table[(r2, c2)][1].update(table[(r1, c1)][1])
        for (i, j) in table[(r1, c1)][1]: table[(i, j)][0] = val
        for (i, j) in table[(r2, c2)][1]: table[(i, j)][0] = val
                 
    def unmerge(r, c):
        for (i, j) in table[(r, c)][1]: 
            table.pop((i, j))
        table[(r, c)][1] = set()
    
    def _print(r, c):
        if (r, c) in table: answer.append(table[(r, c)][0])
        else: answer.append("EMPTY")
        
        
    for command in commands:
        print(command)
        com_lst = command.split()
        if com_lst[0] == 'UPDATE':
            if len(com_lst) == 4: 
                update1(*com_lst[1:])
            else: 
                update2(*com_lst[1:]) 
                for key, val in table.items(): print(key, val)
        elif com_lst[0] == 'MERGE': 
            merge(*com_lst[1:])
            for key, val in table.items(): print(key, val)
        elif com_lst[0] == 'UNMERGE': 
            unmerge(*com_lst[1:])
            for key, val in table.items(): print(key, val)
        else: 
            _print(*com_lst[1:])
    
    print(answer)
    return answer


# solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"])
solution(["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"])
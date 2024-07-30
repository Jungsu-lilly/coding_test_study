# https://www.acmicpc.net/problem/

'''
1. 아이디어 :
    union-find
2. 시간복잡도 :
    O(n * commands)
3. 자료구조 :
    해시맵
'''

from collections import defaultdict


def solution(commands):
    table = [["" for _ in range(50)] for _ in range(50)]
    par = {(row, col): (row, col) for row in range(50) for col in range(50)}
    rank = {(row, col): 1 for row in range(50) for col in range(50)}
    value = defaultdict(str) #cord, value

    def find(x):
        if x != par[x]:
            par[x] = find(par[x])
        return par[x]

    def union(a, b):
        ra = find(a)
        rb = find(b)
        if ra == rb:
            return ra

        if ra != rb:
            if rank[ra] > rank[rb]:
                par[rb] = ra
                return ra
            elif rank[ra] < rank[rb]:
                par[ra] = rb
                return rb
            else:
                par[rb] = ra
                rank[ra] += 1
                return ra

    ans = []

    for cmd in commands:
        cmd = cmd.split()
        if cmd[0] == "UPDATE" and len(cmd) == 4:
            row, col = int(cmd[1]) - 1, int(cmd[2]) - 1
            root = find((row, col))
            value[root] = cmd[3]
        elif cmd[0] == "UPDATE" and len(cmd) == 3:
            value1, value2 = cmd[1], cmd[2]
            for key in value:
                if value[key] == value1:
                    value[key] = value2
        elif cmd[0] == "MERGE":
            row1, col1, row2, col2 = int(cmd[1]) - 1, int(cmd[2]) - 1, int(cmd[3]) - 1, int(cmd[4]) - 1
            ra, rb = find((row1, col1)), find((row2, col2))
            if ra != rb:
                root = union((row1, col1), (row2, col2))
                merged_value = value[ra] if value[ra] else value[rb]
                value[root] = merged_value
        elif cmd[0] == "UNMERGE":
            row, col = int(cmd[1]) - 1, int(cmd[2]) - 1
            root = find((row, col))
            prev = value[root]
            unmerge_list = [k for k, v in par.items() if find(k) == root]
            for cell in unmerge_list:
                par[cell] = cell
                value[cell] = ""
            value[(row,col)] = prev
        elif cmd[0] == "PRINT":
            row, col = int(cmd[1])-1, int(cmd[2])-1
            root = find((row, col))
            ans.append(value[root] if value[root] else "EMPTY")
    return ans

# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


def solution(n, l, r):
    l-=1
    r-=1
    length = 5 ** n
    total_ones = 4 ** n

    def count_ones(start, end):
        count = 0
        for i in range(start, end+1):
            if i % 5 != 2:
                count+=1
        return count

    def dfs(num, idx, rep, start, end): # "1"/"0", idx, 구간 시작, 구간 끝, 1의 개수를 계산하는 범위
        if start > r or end < l:  # 범위 밖일때 1의 갯수 0
            return 0
        if rep == n:  # 범위에 걸쳐있을떄
            if num == "0":
                return 0
            else:
                #걸쳤을때 범위 구하기 예: 현재 범위 15~19, l=4, r=17이면 15~17까지 구함
                temp_start = max(l, start)
                temp_end = min(r, end)
                return count_ones(temp_start, temp_end)

        # 현구간의 크기
        block_size = (end - start + 1) // 5

        if num == "1":
            return dfs("1", 0, rep + 1, start, start + block_size - 1) + \
                dfs("1", 1, rep + 1, start + block_size, start + 2 * block_size - 1) + \
                dfs("0", 2, rep + 1, start + 2 * block_size, start + 3 * block_size - 1) + \
                dfs("1", 3, rep + 1, start + 3 * block_size, start + 4 * block_size - 1) + \
                dfs("1", 4, rep + 1, start + 4 * block_size, end)
        else:
            return 0

    return dfs("1", 0, 0, 0, length - 1)


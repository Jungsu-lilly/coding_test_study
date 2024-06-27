'''
1. 아이디어 :
    dfs로 풀 수 있다
2. 시간복잡도 :
    O( n^2 log n )
3. 자료구조 :
    -
'''

def solution(arr):

    def recur(x, y, n):
        base = arr[x][y]
        for row in range(x, x+n):
            for col in range(y, y+n):
                if arr[row][col] != base:
                    n = n // 2
                    recur(x, y, n) # topleft
                    recur(x+n, y, n) # botleft
                    recur(x, y+n, n) # topright
                    recur(x+n, y+n, n) #botright
                    return
        ans[base] += 1

    ans = [0,0]
    recur(0, 0, len(arr))
    return ans
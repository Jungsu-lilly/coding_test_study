# https://www.acmicpc.net/problem/

'''
1. 아이디어 :
    bfs
2. 시간복잡도 :
    O( n*m )
3. 자료구조 :
    배열
'''

def solution(grid):
    n = len(grid)
    m = len(grid[0])
    # 0: up, 1: right, 2: down, 3: left
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    def get_dir(char, dir):
        if char == "S":
            return dir
        elif char == "L":
            return (dir - 1) % 4
        elif char == "R":
            return (dir + 1) % 4

    def next_cord(x, y, dir):
        x2, y2 = directions[dir]
        nx, ny = x + x2, y + y2
        if nx < 0:
            nx = n - 1
        elif nx >= n:
            nx = 0
        if ny < 0:
            ny = m - 1
        elif ny >= m:
            ny = 0
        return nx, ny

    visited = [[[False, False, False, False] for _ in range(m)] for _ in range(n)]

    def bfs(startX, startY, startDir):
        curr_x, curr_y, curr_dir = startX, startY, startDir
        count = 0

        while not visited[curr_x][curr_y][curr_dir]:
            visited[curr_x][curr_y][curr_dir] = True
            count += 1

            curr_dir = get_dir(grid[curr_x][curr_y], curr_dir)
            curr_x, curr_y = next_cord(curr_x, curr_y, curr_dir)

        return count

    ans = []
    for row in range(n):
        for col in range(m):
            for direction in range(4):
                if not visited[row][col][direction]:
                    ans.append(bfs(row, col, direction))

    return sorted(ans)

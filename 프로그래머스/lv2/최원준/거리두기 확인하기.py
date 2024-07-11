'''
1. 아이디어 :
    P1와 P2 사이의 X가 존재하는지 확인하는 방법은 bfs를 통해서 확인할 수 있다.
    P1부터 상하좌우로 뻗어나갈때 경로에 X가 존재하면 P2까지 도달할 수 없다.
    bfs 조건으로, P1부터 거리가 3이상이거나, "X"를 마주치면 멈추지만, 아니라면 큐에 넣는다
2. 시간복잡도 :
    O( 5*5*5 )
3. 자료구조 :
    배열, 큐
'''


from collections import deque

def solution(places):
    def bfs(row, col, place):
        queue = deque()
        queue.append((row, col, 0))
        place[row][col] = "X"

        while queue:
            r1, c1, distance = queue.popleft()
            if distance > 2:
                continue
            if place[r1][c1] == "P":
                return False
            place[r1][c1] = "X"

            for r2, c2 in dir:
                nr, nc = r1 + r2, c1 + c2
                if not (0 <= nr < 5 and 0 <= nc < 5) or place[nr][nc] == "X":
                    continue
                queue.append((nr, nc, distance + 1))
        return True

    def check_place(place):
        place = [list(place[i]) for i in range(len(place))]
        for row in range(5):
            for col in range(5):
                if place[row][col] == "P" and not bfs(row, col, place):
                    return 0
        return 1

    dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    return [check_place(place) for place in places]


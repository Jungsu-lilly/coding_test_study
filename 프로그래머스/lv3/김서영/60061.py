def solution(n, build_frame):
    """
    :n:벽면 크기
    :build_frame[[x,y,a,b]]: (x,y) 기둥/보 설치/삭제할 좌표
                                a : 0 기둥, 1 보
                                b : 0 삭제, 1 설치
    """
    answer = [[]]
    def check_build_column(x, y):
        """
        - valid column) 바닥 위 or 보 한쪽 끝 위 or 다른 기둥 위
        """
        flag = False
        if y==0: flag = True
        for dx, dy in [[-1, 0], [-1, -1]]:
            nx, ny = x+dx, y+dy
            if 0<=nx<n+1 and 0<=ny<n+1 and frame[nx][ny]==1:
                flag = True
        if 0<=y-1 and frame[x][y-1] == 0: flag = True
        return flag
        
            
    def check_build_beam(x, y):
        """
        - valid beam) 한쪽 끝이 기둥 위 or 양쪽 끝이 다른 보와 동시에 연결
        """
        flag = False
        for dx, dy in [[0, -1], [1, -1]]:
            nx, ny = x+dx, y+dy
            if 0<=nx<n+1 and 0<=ny<n+1 and frame[nx][ny] == 0:
                flag = True
        if 0<=x-1 and x+1<n+1 and frame[x-1][y]==1 and frame[x+1][y]==1: 
            flag = True
        return flag
    
    def remove_check(x, y):
        pass
    
    
    frame = [[-1 for _ in range(n+1)] for _ in range(n+1)]
    for x, y, a, b in build_frame:
        if b == 1: # 설치
            if a == 0 and check_build_column(x, y): frame[x][y] = 0
            else:   
                if check_build_beam(x, y): frame[x][y] = 1
        else: # 삭제 - 남은 구조물이 valid_check 통과해야함
            remove_check(x, y)
                
    return [[i, j, frame[i][j]] for i in range(n+1) for j in range(n+1) if frame[i][j]!=-1 ]

"""
쌈@뽕 깔끔한 풀이..
- is_bo, is_build 유의미한 변수로 받기
- n*n frame만들어서 인덱스로 접근, 행렬에 값 넣지 않고 해시셋으로 (좌표, bo/collar) 값만 들고다니기
    - 전체 bo/collar 인 좌표만 깔끔하게 들고있고 삭제 조건도 얘네만 한번 싹 검사하면 됨
"""
def solution(n, build_frame):
    def insert_check(x, y, is_bo):
        if not is_bo: #collar
            bottom_collar = (x, y-1, 0)
            left_bo, right_bo = (x-1, y, 1), (x, y, 1)
            return True if y == 0 or \
                bottom_collar in built_set or \
                    left_bo in built_set or \
                        right_bo in built_set else False
        elif is_bo: #bo
            left_collar, right_collar = (x, y-1, 0), (x+1, y-1, 0)
            left_bo, right_bo = (x-1, y, 1), (x+1, y, 1)
            return True if left_collar in built_set or \
                right_collar in built_set or \
                    (left_bo in built_set and right_bo in built_set) else False

    def remove_check(x, y, is_bo):
        built_set.remove((x, y, is_bo))
        for x2, y2, is_bo2 in list(built_set):
            if not insert_check(x2, y2, is_bo2):
                built_set.add((x, y, is_bo))
                return False
        built_set.add((x, y, is_bo))
        return True

    built_set = set()
    for x, y, is_bo, is_insert in build_frame:
        if is_insert and insert_check(x, y, is_bo):
            built_set.add((x,y,is_bo))
        elif not is_insert and remove_check(x, y, is_bo):
            built_set.remove((x,y,is_bo))

    return sorted(list(built_set))
def solution(n, build_frame):
    """
    :n:벽면 크기
    :build_frame[[x,y,a,b]]: (x,y) 기둥/보 설치/삭제할 좌표
                                a : 0 기둥, 1 보
                                b : 0 삭제, 1 설치
    """
    answer = [[]]
    def check_column(x, y):
        """
        - valid column) 바닥 위 or 보 한쪽 끝 위 or 다른 기둥 위
        """
        if x==0: return True
        for dx, dy in [[-1, 0][1, 0]]:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<n and 
    
    def check_beam(x, y):
        """
        - valid beam) 왼쪽 끝이 기둥 위 or 양쪽 끝이 다른 보와 동시에 연결
        """
        pass
    
    
    frame = [[-1 for _ in range(n)] for _ in range(n)]
    for x, y, a, b in build_frame:
        if a == 0 and check_column(x, y): frame[x][y] = 0
        else:   
            if frame[x][y] > -1: continue
            if check_beam(x, y): frame[x][y] = 1
        
    
    return answer
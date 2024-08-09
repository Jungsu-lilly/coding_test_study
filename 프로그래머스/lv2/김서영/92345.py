"""
[Snippet]
(discard, just initial approach)
- A 이동좌표, B 이동좌표 -> 이 length 가장 긴게 답
- board 좌표 다 넣어놓고
        A 이동좌표, B 이동좌표 pop 
        backtrack() : 현재 상황노드에서 게임 진행 시 캐릭터 움직인 횟수 구해서 답 업데이트
        다시 board에 좌표 넣기
        
[Final Idea]
- 승패를 이동횟수로 결정한다. : 이동횟수가 홀수면 승리 짝수면 패배
- dfs로 두 플레이어 번갈아가면서 각 턴에서 상/하/좌/우 중 가능한 선택을 한다(=재귀 보내기),
    - 리턴받은 값(현재 노드에 달린 자식들 depth)은 해당 선택을 한 이후 경기 종료까지 플레이어 이동 횟수다.
    - 이를 
- 복구 : 이동 위치 선택 후 다른 선택을 하기 전 이전 선택을 복원한다.
"""

def solution(board, aloc, bloc):
    
    def backtrack(x1, y1, x2, y2):
        if board[x1][y1] == 0: return 0
        board[x1][y1] = 0
        
        ret = 0 
        for dx, dy in zip(move[0], move[1]):
            nx, ny = x1+dx, y1+dy
            if nx<0 or nx>=len(board) or ny<0 or ny>=len(board[0]):
                continue
            if board[nx][ny] == 0:
                continue

            cnt = 1 + backtrack(x2, y2, nx, ny)
            
                                        # 짝수면 패배, 홀수면 승리
            if ret % 2 == 0:            # 지는 줄 알았음
                if cnt % 2 == 0:                # 진다. 최대한 도망가야함
                    ret = max(ret, cnt)
                else:                           # 새로 들어온 케이스가 이기는 케이스. 그럼 이겨야지
                    ret = cnt
            else:                       # 이기는 줄 알았음 - 지는 케이스 무시
                if cnt % 2 == 1:                # 새로 들어온 케이스가 이기는 케이스 - 적게 움직여서 이겨야지
                    ret = min(ret, cnt)
            
        board[x1][y1] = 1  # 복구
        return ret
        
    move = [[-1, 1, 0, 0], [0, 0, -1, 1]]
    return backtrack(aloc[0], aloc[1], bloc[0], bloc[1])
        

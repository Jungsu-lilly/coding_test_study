def solution(board):
    """
    - (O개수==X개수 or O개수+1==X개수) 를 만족하지 않는 경우 0
    - (O승리 and X승리) 안 경우 0
    - 1
    """
    for b in board: print(b)
    def is_valid_num_of_sign() -> bool:
        n_o, n_x = len(o_coor), len(x_coor)
        return (n_o==n_x or n_o==n_x+1)
    
    def is_winner(sign: set)-> bool:
        """
        sign 좌표리스트 받아서 해당 sign이 이겼는지 여부 리턴
        
        """
        win_Case = (
            {(0, 0), (0, 1), (0, 2)},
            {(1, 0), (1, 1), (1, 2)},
            {(2, 0), (2, 1), (2, 2)},
            {(0, 0), (1, 0), (2, 0)},
            {(0, 1), (1, 1), (2, 1)},
            {(0, 2), (1, 2), (2, 2)},
            {(0, 0), (1, 1), (2, 2)},
            {(0, 2), (1, 1), (2, 0)}
        )
        return sign in win_Case
        
        
    o_coor, x_coor = set(), set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O': o_coor.add((i, j))
            elif board[i][j] == 'X': x_coor.add((i, j))


    if not is_valid_num_of_sign(): return 0
    if is_winner(o_coor) and is_winner(x_coor): return 0
    if is_winner(o_coor) and len(o_coor)>3: return 0
    if is_winner(x_coor) and len(x_coor)>3: return 0

    return 1

solution(["O.X", ".O.", "..X"])
solution(["OOO", "...", "XXX"])
solution(["...", ".X.", "..."])
solution(["...", "...", "..."])
# https://school.programmers.co.kr/learn/courses/30/lessons/92345
import sys

def moveable(board, player):
    able = []
    x, y = player
    moves = [(x, y+1), (x, y-1), (x-1, y), (x+1, y)]
    for move in moves:
        nx, ny = move
        if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] == 1:
            able.append(move)
    return able

def minimax(board, aloc, bloc, isMaximizing):
    current_loc = aloc if isMaximizing else bloc
    able_movements = moveable(board, current_loc)
    
    if not able_movements:
        return 0

    best_score = sys.maxsize if isMaximizing else -sys.maxsize-1
    
    for move in able_movements:
        board[current_loc[0]][current_loc[1]] = 0
        
        if isMaximizing:
            score = 1 + minimax(board, move, bloc, False)
            best_score = min(best_score, score)
        else:
            score = 1 + minimax(board, aloc, move, True)
            best_score = max(best_score, score)
        
        board[current_loc[0]][current_loc[1]] = 1
    
    return best_score

def solution(board, aloc, bloc):
    print(minimax(board, aloc, bloc, False), minimax(board, aloc, bloc, True))
    return minimax(board, aloc, bloc, False)

board = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]
aloc = [1, 0]
bloc = [1, 2]

# board = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
# aloc = [1,0]
# bloc = [1,2]

# board = [[1, 1, 1, 1, 1]]
# aloc = [0,0]
# bloc = [0,4]

# board = [[1]]
# aloc = [0,0]
# bloc = [0,0]

print(solution(board, aloc, bloc))
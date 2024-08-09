#include <string>
#include <vector>
#include <iostream>

using namespace std;

int dx[4] = { 0, 0, -1, 1 };
int dy[4] = { -1, 1, 0, 0 };

int answer = -1;

int row;
int col;

void Move(vector<vector<int>>& board, vector<int> loc, vector<int> nextLoc, int moveCnt)
{
    ++moveCnt;

    for (int dCnt = 0; dCnt < 4; ++dCnt)
    {
        int nextY = loc[0] + dy[dCnt];
        int nextX = loc[1] + dx[dCnt];

        if (nextX < 0 || nextY < 0 || nextX >= col || nextY >= row || board[nextY][nextX] == 0)
        {
            answer = max(answer, moveCnt - 1);
            continue;
        }

        board[loc[0]][loc[1]] = 0;

        Move(board, nextLoc, { nextY, nextX }, moveCnt);

        board[loc[0]][loc[1]] = 1;
    }


}

int solution(vector<vector<int>> board, vector<int> aloc, vector<int> bloc) {

    row = board.size();
    col = board[0].size();

    Move(board, aloc, bloc, 0);

    return answer;
}
#include <string>
#include <vector>
#include <iostream>

using namespace std;

// 1. 스킬에 따라 벽 내구도 낮추고, 높이고.. 
// 2. 마지막에 벽 내구도 0 초과한 것들 개수 반환
// 효율성 0 시간초과

void do_skill(int type, int r1, int c1, int r2, int c2, int degree, vector<vector<int>> &board) {
    
    if (type == 1) {
        degree = -degree;
    }
    for (int row = r1; row <= r2; ++row) {
        for (int col = c1; col <= c2; ++col) {
            board[row][col] += degree;
        }
    }
}

int solution(vector<vector<int>> board, vector<vector<int>> skill) {

    for (auto s : skill) {
        do_skill(s[0], s[1], s[2], s[3], s[4], s[5], board);
    }
    
    int answer = 0;
    for (auto b : board) {
        for (auto e : b) {
            if (e > 0) {
                ++answer;
            }
        }
    }
    return answer;
}

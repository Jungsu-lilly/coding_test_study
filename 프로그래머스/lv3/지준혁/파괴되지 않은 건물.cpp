#include <string>
#include <vector>
#include <iostream>

using namespace std;

int cumSum[1004][1004];

// 누적합을 이용해서 시간복잡도 O(n^2) 으로 단축
void do_skill(int type, int r1, int c1, int r2, int c2, int degree) {
    
    degree = type == 1 ? degree * -1 : degree;
    
    cumSum[r1][c1] += degree; // 시작점
    cumSum[r1][c2 + 1] -= degree; // 열 경계
    cumSum[r2 + 1][c1] -= degree; // 행 경계
    cumSum[r2 + 1][c2 + 1] += degree; // 복구 
}

int solution(vector<vector<int>> board, vector<vector<int>> skill) {

    for (auto s : skill) {
        do_skill(s[0], s[1], s[2], s[3], s[4], s[5]);
    }

    for (int i = 0; i <= board.size(); ++i) {
        for (int j = 0; j < board[0].size(); ++j) {
            cumSum[i][j + 1] += cumSum[i][j];
        }
    }    
    
    for (int j = 0; j <= board[0].size(); ++j) {
        for (int i = 0; i < board.size(); ++i) {
            cumSum[i + 1][j] += cumSum[i][j];
        }
    }

    int ans = 0;
    for (int i = 0; i < board.size(); ++i) {
        for (int j = 0; j < board[0].size(); ++j) {
            if (board[i][j] + cumSum[i][j] > 0) ++ans;
        }
    }

    return ans;
}

// [solve] 초기 풀이 n^3 1000 * 1000 * 250,000
// 1. 스킬에 따라 벽 내구도 낮추고, 높이고..
// 2. 마지막에 벽 내구도 0 초과한 것들 개수 반환
// 효율성 0 시간초과
// 
// void do_skill(int type, int r1, int c1, int r2, int c2, int degree, vector<vector<int>> &board) {
// 
//     if (type == 1) {
//         degree = -degree;
//     }
//     for (int row = r1; row <= r2; ++row) {
//         for (int col = c1; col <= c2; ++col) {
//             board[row][col] += degree;
//         }
//     }
// }
// 
// int solution(vector<vector<int>> board, vector<vector<int>> skill) {
// 
//     for (auto s : skill) {
//         do_skill(s[0], s[1], s[2], s[3], s[4], s[5], board);
//     }
// 
//     int answer = 0;
//     for (auto b : board) {
//         for (auto e : b) {
//             if (e > 0) {
//                 ++answer;
//             }
//         }
//     }
//     return answer;
// }

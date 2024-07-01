#include <string>
#include <vector>
#include <iostream>

using namespace std;

char b[32][32];

bool is_boom(int h, int w, int& ans) {
    bool is_boom = false;
    bool is_checked[32][32] = {};
    for (int i = 0; i < h; ++i) {
        for (int j = 0; j < w; ++j) {
            char c = b[i][j];
            if (c != '!' && b[i][j + 1] == c && b[i + 1][j] == c && b[i + 1][j + 1] == c) {
                is_boom = true;
                is_checked[i][j] = true;
                is_checked[i][j + 1] = true;
                is_checked[i + 1][j] = true;
                is_checked[i + 1][j + 1] = true;
            }
        }
    }
    for (int i = 0; i < h; ++i) {
        for (int j = 0; j < w; ++j) {
            if (is_checked[i][j]) {
                b[i][j] = '!';
                ++ans;
            }
        }
    }
    return is_boom;
}

void recur(int i, int j, int h) {
    if (b[i][j] == '!' || b[i + 1][j] != '!' || i == h - 1) 
        return;
    b[i + 1][j] = b[i][j];
    b[i][j] = '!';
    recur(i + 1, j, h);
}

void down(int h, int w) {
    for (int j = 0; j < w; ++j) {
        for (int i = h - 1; i >= 0; --i) {
            recur(i, j, h);
        }
    }
}

int solution(int m, int n, vector<string> board) {
    
    for (int i = 0; i < board.size(); ++i) {
        for (int j = 0; j < board[j].size(); ++j) {
            b[i][j] = board[i][j];
        }
    }
    
    int ans = 0;
    while (true) {
        if (!is_boom(m, n, ans))
            break;
        down(m, n);
    }
    return ans;
}

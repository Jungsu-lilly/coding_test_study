#include <string>
#include <iostream>
using namespace std;

int dy[] = {1, 0, -1, 0};
int dx[] = {0, 1, 0, -1};

bool is_visited[14][14][4];

// 방향까지 검사
// 방향 검사할 때 출발지 방향 체크했으면 반대로도 체크하여 중복 계산 막기
int move(string& drs) {
    
    pair<int, int> now = {5, 5};
    
    int dir = 0;
    int ans = 0;
    for (auto& c : drs) {
        
        if (c == 'U') {
            dir = 0;
        } else if (c == 'D') {
            dir = 2;
        } else if (c == 'R') {
            dir = 1;
        } else {
            dir = 3;
        }
        
        int ny = now.first + dy[dir];
        int nx = now.second + dx[dir];
        
        if (ny < 0 || ny > 10 || nx < 0 || nx > 10) 
            continue;
        if (!is_visited[ny][nx][dir]) {
            is_visited[ny][nx][dir] = true;
            is_visited[now.first][now.second][(dir + 2) % 4] = true;
            ++ans;
        }
        now = {ny, nx};
    }  
    return ans;
}

int solution(string dirs) {
    
    return move(dirs);
}

#include <string>
#include <vector>
#include <iostream>
#include <queue>

using namespace std;

// https://school.programmers.co.kr/learn/courses/30/lessons/154538

// 2를 곱하거나 3을 곱하거나 N을 더할 때 최소 연산 횟수 => bfs로 접근
// 1. 종료조건: x가 y와 같을 때, 같은 경우를 발견하지 못할 때 -1
// 2. 큐에다가 가능한 수 넣다뺐다하면서 탐색
// 3. 1'000'000이 넘어간 수는 더 이상 넣지 않음(탐색 안함)

bool is_visited[1'000'004];

int bfs(int x, int y, int n) {
    queue<pair<int, int>> q;

    q.push({x, 0});
    is_visited[x] = true;

    while (!q.empty()) {
        auto [cur_x, cnt] = q.front();
        q.pop();

        if (cur_x == y) {
            return cnt;
        }

        if (cur_x > 1'000'000) {
            continue;
        }

        if (cur_x * 2 <= 1'000'000 && !is_visited[cur_x * 2]) {
            is_visited[cur_x * 2] = true;
            q.push({cur_x * 2, cnt + 1});
        }
        if (cur_x * 3 <= 1'000'000 && !is_visited[cur_x * 3]) {
            is_visited[cur_x * 3] = true;
            q.push({cur_x * 3, cnt + 1});
        }
        if (cur_x + n <= 1'000'000 && !is_visited[cur_x + n]) {
            is_visited[cur_x + n] = true;
            q.push({cur_x + n, cnt + 1});
        }
    }
    return -1;
}

int solution(int x, int y, int n) {
    int answer = 0;
        
    answer = bfs(x, y, n);;
    
    return answer;
}


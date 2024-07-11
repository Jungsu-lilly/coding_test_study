#include <string>
#include <vector>
#include <iostream>
#include <queue>

using namespace std;


// 핵심 -> 정확한 순위를 만들기 위해선 모든 사람과 경기를 해야한다. 경기 횟수 (n - 1)
//
// [플루이드 워샬 알고리즘 -> 아래 사항 처리]
// 1등이 2등을 이기고, 2등이 5등을 이겼다면,
// 1등도 5등을 이겼다고 해야 한다.

// 1등이 3등에게 지고, 3등이 4등에게 졌다면
// 1등도 4등에게 졌다고 해야 한다.

int ret[104][104];
int solution(int n, vector<vector<int>> results) {

    for (auto& e: results) {
        ret[e[0]][e[1]] = 1;
        ret[e[1]][e[0]] = -1;
    }

    for (int k = 1; k <= n; ++k) {
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (ret[i][k] == 1 && ret[k][j] == 1) {
                    ret[i][j] = 1;
                    ret[j][i] = -1;
                }
                if (ret[i][k] == -1 && ret[k][j] == -1) {
                    ret[i][j] = -1;
                    ret[j][i] = 1;
                }
            }
        }
    }

    int ans = 0;
    for (int i = 1; i <= n; ++i) {
        int cnt = 0;
        for (int j = 1; j <= n; ++j) {
            if (ret[i][j]) ++cnt;
        }
        if (cnt == n - 1)
            ++ans;
    }

    return ans;
}

// int deg[104];
// vector<int> adj[104];
// 
// // 1. 위상정렬로 순서 구함.
// // 2. 1번에서 나온 순서로 다시 노드를 돌면서 순서 검증 -> 대략적인 순서는 알 수 있으나 정확한 순위를 구하는 정보를 만들 수 없었음.
// 
// int solution(int n, vector<vector<int>> results) {
// 
//     for (auto& e: results) {
//         adj[e[0]].push_back(e[1]);
//         deg[e[1]]++;
//     }
//     
//     queue<int> q;
//     vector<int> ret;
//     for (int i = 1; i <= n; ++i) {
//         if (deg[i] == 0) {
//             q.push(i);
//         }
//     }
//     
//     while (!q.empty()) {
//         int cur = q.front(); q.pop();
//         ret.push_back(cur);
//         for (auto& nxt : adj[cur]) {
//             deg[nxt]--;
//             if (deg[nxt] == 0) 
//                 q.push(nxt);
//         }        
//     }
//     
//     for (auto& x : ret) {
//         cout << "x: " << x << ' ';
//     }
// 
//     cout << '\n';
// 
//     int ans = 0;
//     
//     return ans;
// }

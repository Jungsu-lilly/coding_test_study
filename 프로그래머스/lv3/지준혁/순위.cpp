#include <string>
#include <vector>
#include <iostream>
#include <queue>


using namespace std;

int deg[104];
vector<int> adj[104];

// 1번까지만..

// 1. 위상정렬로 순서 구함.
// 2. 1번에서 나온 순서로 다시 노드를 돌면서 순서 검증

int solution(int n, vector<vector<int>> results) {

    for (auto& e: results) {
        adj[e[0]].push_back(e[1]);
        deg[e[1]]++;
    }
    
    queue<int> q;
    vector<int> ret;
    for (int i = 1; i <= n; ++i) {
        if (deg[i] == 0) {
            q.push(i);
        }
    }
    
    while (!q.empty()) {
        int cur = q.front(); q.pop();
        ret.push_back(cur);
        for (auto& nxt : adj[cur]) {
            deg[nxt]--;
            if (deg[nxt] == 0) 
                q.push(nxt);
        }        
    }
    
    for (auto& x : ret) {
        cout << "x: " << x << ' ';
    }

    cout << '\n';

    int ans = 0;
    
    return ans;
}

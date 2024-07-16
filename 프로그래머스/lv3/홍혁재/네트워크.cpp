#include <string>
#include <vector>

using namespace std;


bool visited[200] = {false,};
vector<vector<int>> graph;

void dfs(int x) {
    visited[x] = true;
    
    for(int i = 0; i < graph[x].size(); i++) {
        if(graph[x][i] == 1 && !visited[i]) {
            dfs(i);
        }
    }
}


int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    graph = computers;
    
    // i <- from 0 to n 으로 돌면서 visited가 false인 것만 골라서 다님
    // : visited가 false이면 answer++하고 dfs ㄱㄱ
    for(int i = 0; i < n; i++) {
        if(!visited[i]) {
            answer++;
            dfs(i);
        }
    }
    
    
    return answer;
}
#include <string>
#include <vector>

using namespace std;

// 자연수 n개로 이루어진 중복 집합!!
// 자연수 2개로 이루어진 집합 중 합이 9가 되는 집합 -> {1, 8}, {2, 7}, {3, 6}, {4, 5} 
// 자연수 3개로 이루어진 집합 중 합이 9가 되는 집합 -> {1, 1, 1}, {1, 1, 7}, {1, 2, 6}, {1, 3, 5} ...
// 자연수 4개로 이루어진 집합 중 합이 9가 되는 집합 -> {1, 1, 1, 6} 

// 1. 각 원소의 합이 S가 되면서, 원소의 곱이 최대가 되어야 한다.
// 2. 먼저 가능한 원소 수를 구해야함. n개 뽑아야 함. -> DFS
// 3. N개의 원소를 합해서 합이 S가 나오는 순열 구함.
// 4. 최대값을 갱신할 때 순열도 갱신해서 <answer>로 반환함.

int is_selected[10'004];
int max_value
vector<int> answer; 
void dfs(int depth, int sum, int n, int s) {
    
    if (depth == n && sum == s) {
    }
}

vector<int> solution(int n, int s) {
    vector<int> answer;
    
    dfs(0, n, s)
    return answer;
}

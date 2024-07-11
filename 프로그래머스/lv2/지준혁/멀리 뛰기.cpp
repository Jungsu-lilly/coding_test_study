#include <string>
#include <vector>
#include <iostream>

using namespace std;

// dp 풀이
// 1 2 3 5 8 ...
int dp[2004];

long long solution(int n) {

    dp[1] = 1;
    dp[2] = 2;
    for (int i = 3; i <= n; ++i) {
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567;
    }
    return dp[n];
}

// 처음 풀이 2^2000 -> 시간 초과
long long ans = 0;

void dfs(int depth, int sum, int bound) {
    if (depth > bound || sum > bound) {
        return;
    }
    if (sum == bound) {
        ++ans %= 1234567;
        return;
    }
    for (int step = 1; step <= 2; ++step) {
        dfs(depth + 1, sum + step, bound);
    }
}
long long solution(int n) {
    dfs(0, 0, n);
    return ans;
}

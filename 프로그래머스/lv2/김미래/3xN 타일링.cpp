#include <string>
#include <vector>
using namespace std;

int solution(int n) {
    if (n % 2 != 0) return 0; 

    long long dp[5001] = {0}; 
    dp[0] = 1;                
    dp[2] = 3;                

    for (int i = 4; i <= n; i += 2) {
        dp[i] = 3 * dp[i-2];
        for (int j = i - 4; j >= 0; j -= 2) {
            dp[i] += 2 * dp[j];
        }
    }

    return dp[n]; 
}

import java.util.*;

// dp[i] = i원을 만들기위한 동전의 수, dp[0] = 1 -> 1 2 3원 
// dp[1] = 1;
// dp[2] = 2(1) + 1(2) = 3;
// dp[3] = 3(1) + 1(3) = 4;
// dp[4] = dp[3] + 1
// dp[5] = dp[2] + 3
//
// 위의 방식대로 계산한다면 중복 계산이 된다. 아래 처럼 각 동전마다 1원씩 증가시키며 하나씩 더하는 방식이다.
// coin: 2 -> dp[1] = 1; dp[2] = 1; dp[3] = 1; dp[4] = 1; dp[5] = 1;
// coin: 3 -> dp[2] = 2; dp[3] = 2; dp[4] = 3; dp[5] = 3;
// coin: 5 -> dp[5] = 3 + 1 = 4;
class Solution {
    
    int[] dp = new int[100_004];
    
    public int solution(int n, int[] money) {
        
        dp[0] = 1;
        for (var coin : money) {
            for (int i = coin; i <= n; ++i) {
                dp[i] += dp[i - coin];
                dp[i] %= 1_000_000_007;
            }
        }
        return dp[n];
    }
}

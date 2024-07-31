// 모든 문제를 풀수있는 알고력과 코딩력을 만드는데 드는 최단시간

import java.util.*;
class Solution {
    public int solution(int alp, int cop, int[][] problems) {
        int max_alp_req = 0;
        int max_cop_req = 0;
        
        for (int[] problem : problems) {
            max_alp_req = Math.max(max_alp_req, problem[0]);
            max_cop_req = Math.max(max_cop_req, problem[1]);
        }
        
        if (max_alp_req <= alp && max_cop_req <= cop) {
            return 0;
        }
        
        if (alp > max_alp_req) {
            alp = max_alp_req;
        }
        if (cop > max_cop_req) {
            cop = max_cop_req;
        }
        
        int[][] dp = new int[max_alp_req + 1][max_cop_req + 1];
        for (int i = 0; i < dp.length; i++) {
            for (int j = 0; j < dp[0].length; j++) {
                dp[i][j] = Integer.MAX_VALUE;
            }
        }
        
        dp[alp][cop] = 0;
        
        for (int i = alp; i <= max_alp_req; i++) {
            for (int j = cop; j <= max_cop_req; j++) {
                if (i < max_alp_req) {
                    dp[i + 1][j] = Math.min(dp[i + 1][j], dp[i][j] + 1);
                }
                if (j < max_cop_req) {
                    dp[i][j + 1] = Math.min(dp[i][j + 1], dp[i][j] + 1);
                }
                for (int[] problem : problems) {
                    if (i >= problem[0] && j >= problem[1]) {
                        int new_alp = Math.min(i + problem[2], max_alp_req);
                        int new_cop = Math.min(j + problem[3], max_cop_req);
                        dp[new_alp][new_cop] = Math.min(dp[new_alp][new_cop], dp[i][j] + problem[4]);
                    }
                }
            }
        }
        
        return dp[max_alp_req][max_cop_req];
    }
}

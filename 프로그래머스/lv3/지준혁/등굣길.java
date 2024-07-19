import java.util.*;

class Solution {
    
    public int solution(int m, int n, int[][] puddles) {
        
        int[][] map = new int[n][m];
        int[][] memo = new int[n][m]; 
        
        for (int i = 0; i < puddles.length; ++i) map[puddles[i][1] - 1][puddles[i][0] - 1] = 1;
        
        for (int i = 0; i < n; ++i) Arrays.fill(memo[i], -1);

        return goToSchool(0, 0, n, m, map, memo);
    }
    
    int goToSchool(int y, int x, int r, int c, int[][] map, int[][] memo) {
        
        if (y >= r || x >= c || map[y][x] == 1)
            return 0;
        
        if (y == r - 1 && x == c - 1)
            return 1;
        
        if (memo[y][x] != -1)
            return memo[y][x];
        
        memo[y][x] = (goToSchool(y + 1, x, r, c, map, memo) + goToSchool(y, x + 1, r, c, map, memo)) % 1_000_000_007;
        
        return memo[y][x];
    }
}

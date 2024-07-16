import java.util.*;

class Solution {
    public int solution(int n, int[][] computers) {
        
        int[] p = new int[n];
        Arrays.fill(p, -1);
        
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (computers[i][j] == 1) {
                    unionByRank(i, j, p);
                }
            }
        }
        
        Set<Integer> ans = new HashSet<>();
        for (int i = 0; i < n; ++i) {
            ans.add(find(i, p));
        }
        
        return ans.size();
    }
    
    int find(int x, int[] p) {
	if (p[x] < 0) return x;
	else return p[x] = find(p[x], p);
    }
    
    void unionByRank(int x, int y, int[] p) {
        x = find(x, p);
        y = find(y, p);
        if (x == y) return;
        if (p[x] == p[y]) p[x]--;
        if (p[x] < p[y]) p[y] = x;
        else p[x] = y;
    }
}

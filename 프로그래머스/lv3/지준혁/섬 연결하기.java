import java.util.*;

// 크루스칼 알고리즘
class Solution {
    int[] p;

    public int find(int x) {
        if (p[x] < 0) return x;
        return p[x] = find(p[x]);
    }

    public boolean isUnioned(int x, int y) {
        x = find(x);
        y = find(y);
        if (x == y) return false;
        if (p[x] == p[y]) p[x]--;
        if (p[x] < p[y]) p[y] = x;
        else p[x] = y;
        return true;
    }

    public int solution(int n, int[][] costs) {
        p = new int[n];
        Arrays.fill(p, -1);
        Arrays.sort(costs, (a, b) -> Integer.compare(a[2], b[2]));
        int ans = 0;
        int cnt = 0;
        for (var c : costs) { // a, b, cost
            if (!isUnioned(c[0], c[1]))
                continue;
            ans += c[2];
            ++cnt;
            if (cnt == n - 1) break;
        }
        return ans;
    }
}

import java.util.*;

class Solution {
    
    int[] dy = {-1, 0, 1, 0};
    int[] dx = {0, 1, 0, -1};
    public int solution(int[][] maps) {
        
        return bfs(maps);
    }
    
    int bfs(int[][] maps) {
        
        int n = maps.length;
        int m = maps[0].length;
        int[][] dist = new int[n][m];
        for (int i = 0; i < n; i++) Arrays.fill(dist[i], -1);
        Queue<int[]> q = new LinkedList<>();
    
        dist[0][0] = 1;
        q.offer(new int[]{0, 0});
        
        while (!q.isEmpty()) {
            var cur = q.poll();
            for (int dir = 0; dir < 4; ++dir) {
                int ny = cur[0] + dy[dir];
                int nx = cur[1] + dx[dir];
                
                if (ny < 0 || ny >= n || nx < 0 || nx >= m) continue;
                if (maps[ny][nx] == 0 || dist[ny][nx] != -1) continue;
                dist[ny][nx] = dist[cur[0]][cur[1]] + 1;
                q.offer(new int[]{ny, nx});
            }
        }

        return dist[n - 1][m - 1];
    }
}

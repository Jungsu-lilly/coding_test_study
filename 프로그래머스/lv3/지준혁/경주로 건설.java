import java.util.*;

// 헤멘 부분: 현재 경로가 이전 경로보다 비용이 낮을 때만 탐색하도록 했는데, 현재 경로가 더 높더라도 커브 횟수가 낮아 비용이 낮아질 수 있는 반례 존재. -> 비용 경로에 방향까지 저장하여 해결
class Solution {
    int dy[] = {1, 0, -1, 0};
    int dx[] = {0, 1, 0, -1};
    int ans = Integer.MAX_VALUE;
    
    void bfs(int[][] board) {
        int r = board.length;
        int c = board[0].length;
        int[][][] costs = new int[r][c][4];
        for (int i = 0; i < r; ++i) {
            for (int j = 0; j < c; ++j) {
                Arrays.fill(costs[i][j], Integer.MAX_VALUE);
            }
        }
        
        Queue<int[]> q = new LinkedList<>(); // y, x, cost, dir
        q.add(new int[]{0, 0, 0, -1});
        while (!q.isEmpty()) {
            var cur = q.poll();
            int y = cur[0];
            int x = cur[1];
            int cost = cur[2];
            int d = cur[3];
            
            if (y == r - 1 && x == c - 1) {
                ans = Math.min(ans, costs[y][x][d]);
                continue;
            }
            for (int dir = 0; dir < 4; ++dir) {
                int ny = y + dy[dir];
                int nx = x + dx[dir];
                int ncost = 0;
                if (ny < 0 || ny >= r || nx < 0 || nx >= c) continue;
                if (board[ny][nx] == 1) continue;
                
                if (d == dir || d == -1) ncost += cost + 100;
                else ncost += cost + 600;
                
                if (ncost <= costs[ny][nx][dir]) {
                    costs[ny][nx][dir] = ncost;
                    q.add(new int[]{ny, nx, ncost, dir});
                }
            }
        }
    }
    public int solution(int[][] board) {
        
        bfs(board);
        
        return ans;
    }
}

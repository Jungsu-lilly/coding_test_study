import java.util.*;

// bfs 큐를 이용한다.
// 탐색 거리 2까지 탐색하고, 초기 P가 아닌 P를 만나면 안전하지 않음
// 테케 4개 못맞춤

class Solution {

    int dy[] = {1, 0, -1, 0};
    int dx[] = {0, 1, 0, -1};
    Queue<int[]> q = new LinkedList<>(); // y, x, move
    List<int[]> par = new ArrayList<>(); // y, x
    List<Integer> ans = new ArrayList<>();

    public int[] solution(String[][] places) {

        for (int i = 0; i < places.length; ++i) {
            par.clear();
			q.clear();
            for (int j = 0; j < places[i].length; ++j) {
                for (int k = 0; k < places[i][j].length(); ++k) {
                    if (places[i][j].charAt(k) == 'P') {
                        par.add(new int[]{j, k});
                    }
                }
            }
            boolean isSafe = true;
            for (var e : par) {
                if (!bfs(i, e[0], e[1], places)) {
                    isSafe = false;
                    ans.add(0);
                    break;
                }
            }
            if (isSafe) ans.add(1);
        }

        int[] answer = ans.stream().mapToInt(Integer::intValue).toArray();

        return answer;
    }
    boolean bfs(int i, int y, int x, String[][] places) {

        int r = places[i].length;
        int c = places[i][0].length();
        boolean [][]isVisited = new boolean[5][5];
        int start_y = y;
        int start_x = x;

        isVisited[y][x] = true;
        q.offer(new int[]{y, x, 0});
        while (!q.isEmpty()) {
            var e = q.poll();
            y = e[0];
            x = e[1];
            int move = e[2];
            if (!(start_y == y && start_x == x) && places[i][y].charAt(x) == 'P') return false;
            for (int dir = 0; dir < 4; ++dir) {
                int ny = y + dy[dir];
                int nx = x + dx[dir];
                if (ny < 0 || ny >= r || nx < 0 || nx >= c) continue;
                if (places[i][ny].charAt(nx) == 'X' || isVisited[ny][nx] == true) continue;
                if (move > 1) continue;
                q.offer(new int[]{ny, nx, move + 1});
            }
        }
        return true;
    }
}

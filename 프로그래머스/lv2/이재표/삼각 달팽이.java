import java.util.*;
class Solution {
    public int[] solution(int n) {
        int[][] arr = new int[n][n];
        int[] dx = {0, 1, -1};
        int[] dy = {1, 0, -1};
        int x = 0;
        int y = -1;
        int cnt = 0;
        int dir = 0;
        for (int i = n - 1; i >= 0; i--) {
            for (int j = 0; j <= i; j++) {
                x += dx[dir];
                y += dy[dir];
                if (i == j) {
                    dir = (dir + 1) % 3;
                }
                arr[y][x] = ++cnt;
            }
        }
        int[] answer = new int[n * (n + 1) / 2];
        int index = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= i; j++) {
                if(arr[i][j]!=0){
                    answer[index++] = arr[i][j];
                }
            }
        }
        return answer;
    }
}

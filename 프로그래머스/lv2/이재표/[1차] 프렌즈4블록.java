import java.util.*;
class Solution {
    public class Pos{
        int x;
        int y;
        public Pos(int x,int y){
            this.x=x;
            this.y=y;
        }
    }
    public boolean isRectangle(char[][] board, int x, int y) {
        char b = board[y][x];
        if (x + 1 < board[0].length && y + 1 < board.length &&
            b == board[y][x + 1] && b == board[y + 1][x] && b == board[y + 1][x + 1]) {
            return true;
        }
        return false;
    }
    public int solution(int m, int n, String[] board) {
        char[][] charBoard = new char[m][n];

        for (int i = 0; i < m; i++) {
            charBoard[i] = board[i].toCharArray();
        }

        Queue<Pos> q = new LinkedList<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                q.offer(new Pos(j, i));
                while (!q.isEmpty()) {
                    Pos p = q.poll();
                    if (isRectangle(charBoard, p.x, p.y)) {
                        q.offer(new Pos(p.x + 1, p.y));
                        q.offer(new Pos(p.x, p.y + 1));
                        q.offer(new Pos(p.x + 1, p.y + 1));
                        charBoard[p.y][p.x] = '*';
                    }
                }
            }
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(charBoard[i][j]);
            }
            System.out.println();
        }
        return 1;
    }
}

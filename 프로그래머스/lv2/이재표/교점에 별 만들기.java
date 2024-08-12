import java.util.*;

class Solution {
    public String[] solution(int[][] line) {
        Set<int[]> set = new HashSet<>();

        for (int i = 0; i < line.length; i++) {
            for (int j = i + 1; j < line.length; j++) {
                int A = line[i][0];
                int B = line[i][1];
                int E = line[i][2];

                int C = line[j][0];
                int D = line[j][1];
                int F = line[j][2];

                long under =(long) A * D - (long)B * C;
                if (under == 0) continue; 

                long xi = (long)B * F - (long)E * D;
                long yi =(long) E * C - (long)A * F;

                if (xi % under != 0 || yi % under != 0) continue; 

                int x =(int)( xi / under);
                int y =(int)( yi / under);

                set.add(new int[]{x, y});
            }
        }

        int minX = Integer.MAX_VALUE;
        int maxX = Integer.MIN_VALUE;
        int minY = Integer.MAX_VALUE;
        int maxY = Integer.MIN_VALUE;

        for (int[] p : set) {
            minX = Math.min(minX, p[0]);
            maxX = Math.max(maxX, p[0]);
            minY = Math.min(minY, p[1]);
            maxY = Math.max(maxY, p[1]);
        }

        int width = maxX - minX + 1;
        int height = maxY - minY + 1;

        char[][] grid = new char[height][width];
        for (char[] row : grid) {
            Arrays.fill(row, '.');
        }

        for (int[] p : set) {
            grid[maxY - p[1]][p[0] - minX] = '*';
        }

        String[] answer = new String[height];
        for (int i = 0; i < height; i++) {
            answer[i] = new String(grid[i]);
        }

        return answer;
    }
}

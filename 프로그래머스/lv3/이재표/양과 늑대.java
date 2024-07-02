import java.util.*;
class Solution {
    int[][]board;
    public int solution(int[] info, int[][] edges) {
        int answer = 0;
        int n=info.length;
        board=new int[n][n];
        for(int i=0;i<n;i++){
            Arrays.fill(board[i],-1);
        }
        for(int i=0;i<edges.length;i++){
            board[edges[i][0]][edges[i][1]]=info[i];
        }
        boolean[] visit=new boolean[n];
        visit[0]=true;
        brute(visit,1,0);
        return answer;
    }
    public void brute(boolean[]visit,int cnt,int start){
        for(int i=0;i<board.length;i++){
            if(board[start][i]==-1){
                continue;
            }
        }
    }
}

import java.util.*;
class Solution {
    int[] gInfo;
    int[][]gEdges;
    int maxSheepCnt=0;
    public int solution(int[] info, int[][] edges) {
        gInfo=info;
        gEdges=edges;
        boolean[]visit=new boolean[info.length];
        dfs(0,visit,0,0);
        return maxSheepCnt;
    }
    public void dfs(int idx,boolean[]visit,int sheepCnt,int wolfCnt){
        visit[idx]=true;
        if(gInfo[idx]==0){
            sheepCnt++;
            if(sheepCnt>maxSheepCnt){
                maxSheepCnt=sheepCnt;
            }
        }else{
            wolfCnt++;
        }
        if(sheepCnt<=wolfCnt){
            return;
        }
        for(int[]edge:gEdges){
            if(visit[edge[0]]&& !visit[edge[1]]){
                dfs(edge[1],visit,sheepCnt,wolfCnt);
                visit[edge[1]]=false;
            }
        }
    }
}

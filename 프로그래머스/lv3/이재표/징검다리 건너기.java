import java.util.*;
class Solution {
    public int solution(int n, int[][] costs) {
        int answer = 0;
        PriorityQueue<int[]>pq=new PriorityQueue<>(new Comparator<int[]>(){
            @Override
            public int compare(int[]o1,int[]o2){
                return Integer.compare(o1[1], o2[1]);
            }
        });
        boolean[] visit=new boolean[n];
        int[][]arr=new int[n][n];
        for(int i=0;i<n;i++){
            Arrays.fill(arr[i],-1);
        }
        for(int i=0;i<costs.length;i++){
            arr[costs[i][0]][costs[i][1]]=costs[i][2];
            arr[costs[i][1]][costs[i][0]]=costs[i][2];
        }
        pq.offer(new int[]{0,0});
        int sum=0;
        while(!pq.isEmpty()){
            int[]e=pq.poll();
            if(!visit[e[0]]){
                visit[e[0]]=true;
                answer+=e[1];
                for(int i=0;i<n;i++){
                    if(arr[e[0]][i]!=-1){
                        pq.offer(new int[]{i,arr[e[0]][i]});
                    }
                }
            }
        }
        return answer;
    }
}

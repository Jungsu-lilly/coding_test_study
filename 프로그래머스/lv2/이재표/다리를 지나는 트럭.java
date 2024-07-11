import java.util.*;
class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        Queue<Integer>q=new LinkedList<>();
        for(int i=0;i<bridge_length;i++){
            q.offer(0);
        }
        int sum=0;
        for(int i=0;i<truck_weights.length;i++){
            while(true){
                answer++;
                int cross=q.poll();
                sum-=cross;
                if(sum+truck_weights[i]<=weight){
                    q.offer(truck_weights[i]);
                    sum+=truck_weights[i];
                    break;
                }else{
                    q.offer(0);
                }
            }
        }
        while(!q.isEmpty()){
            q.poll();
            answer+=1;
        }
        return answer;
    }
}

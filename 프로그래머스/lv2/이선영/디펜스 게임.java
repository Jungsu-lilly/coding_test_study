import java.util.*;

class Solution {
  
    public int solution(int n, int k, int[] enemy) {
        int answer = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>((o1,o2)-> o2-o1);
        for(int i=0; i<enemy.length; i++){
            n-=enemy[i];
            pq.offer(enemy[i]);
            
            if(n<0){ // 병사수가 음수일 경우
                if(k>0){ //무적권이 있는 경우
                    n+=pq.poll();
                    k--;
                }else{
                    break;
                }
            }
            answer++;
        }
        
        
        return answer;
    }

}


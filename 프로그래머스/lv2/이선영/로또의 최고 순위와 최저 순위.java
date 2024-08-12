import java.util.*;

class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = new int[2];
        boolean[] flag = new boolean[46];
        
        for(int i=0; i<6; i++){
            flag[win_nums[i]] = true;
        }
        
  
        for(int i=0; i<6; i++){
            int num = lottos[i];

            if(num == 0) {//지워짐
                answer[0]++;
            } else if(flag[num]){ //당첨
                answer[1]++;
                answer[0]++;
            }else{ //낙첨
                continue;
            }
        }
        
        answer[0] = 7-answer[0];
        answer[1] = 7-answer[1];
        if(answer[0] == 7) answer[0] = 6;
        if(answer[1] == 7) answer[1] = 6;
        
        return answer;
    }
}

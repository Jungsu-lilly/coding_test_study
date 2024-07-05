import java.util.*;
class Solution {
    public int solution(int[] stones, int k) {
        int answer = 0;
        // 1 3 4 2 1 0 3 1 4 0 -> 1
        // 0 2 3 1 0 -1 2 0 3 -1 -> 1
        // -1 1 2 0 -1 -2 1 -1 2 -2 -> 1
        // -2 0 1 -1 -2 -3 0 -2 1 -3 -> 1
        while(true){
            int min=Integer.MAX_VALUE;
            for(int i=0;i<stones.length;i++){
                if(min>stones[i] && stones[i]>0){
                    min=stones[i];
                }
            }
            int cnt=0;
            int chk=0;
            for(int i=0;i<stones.length;i++){
                stones[i]-=min;
                if(stones[i]<=0){
                    cnt++;
                }else{
                    cnt=0;
                }
                if(cnt>=k){
                    chk=1;
                }
            }
            answer+=min;
            if(chk!=0){
                break;
            }
        }
        
        return answer;
    }
    public boolean isZeroUnderK(int[]stones,int k){
        int cnt=0;
        for(int i=0;i<stones.length;i++){
            if(stones[i]<=0){
                cnt++;
            }else{
                cnt=0;                
            }
            if(cnt>=k){
                return false;
            }
            
        }
        return true;
    }
}

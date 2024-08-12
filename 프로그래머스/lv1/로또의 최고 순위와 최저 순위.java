import java.util.*;
class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        Arrays.sort(lottos);
        Arrays.sort(win_nums);
        int idx=0;
        int rank=0;
        for(int i=0;i<lottos.length;i++){ //최저등수 구하기
            while(true){
                if(lottos[i]==win_nums[idx]){
                    rank++;
                    idx++;
                    break;
                }else if(lottos[i]<win_nums[idx]){
                    break;
                }else if(lottos[i]>win_nums[idx]){
                    idx++;
                }
            }
        }
        int cnt=0;
        for(int i=0;i<lottos.length;i++){
            if(lottos[i]==0){
                cnt++;
            }
        }
        System.out.println(cnt);
        System.out.println(rank);
        int[]a=new int[]{6,6,5,4,3,2,1};
        int[]answer=new int[]{a[cnt+rank],a[rank]};
        
        return answer;
    }
}

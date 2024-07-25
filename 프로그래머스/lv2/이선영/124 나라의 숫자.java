import java.util.*;

class Solution {
    public String solution(int n) {
        String answer = "";
        StringBuilder sb = new StringBuilder();
        
        while(n>0){
            int num = n%3;
            if(num == 0){ // 4
                sb.insert(0,'4');
                n/=3;
                n--;
            }else{ // 1,2
                sb.insert(0,Integer.toString(num));
                 n /=3;
            }
        }
        
        answer = sb.toString();
        return answer;
    }
}

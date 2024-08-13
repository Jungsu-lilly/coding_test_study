import java.util.*;
class Solution {
    public int solution(String s) {
        int answer = 0;
        char x='-';
        int xcnt=0;
        int cnt=0;
        for(int i=0;i<s.length();i++){
            if(xcnt==0){
                x=s.charAt(i);
                xcnt++;
                continue;
            }
            if(s.charAt(i)==x){
                xcnt++;
            }else{
                cnt++;
            }
            if(xcnt==cnt){
                answer++;
                xcnt=0;
                cnt=0;
            }
        }
        if(xcnt!=0||cnt!=0){
            answer++;
        }
        return answer;
    }
}

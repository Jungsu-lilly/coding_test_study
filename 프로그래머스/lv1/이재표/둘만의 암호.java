import java.util.*;
class Solution {
    public String solution(String s, String skip, int index) {
        String answer = "";
        char[]alp=new char[26];
        for(int i=0;i<26;i++){
            alp[i]=((char)('a'+i));
        }
        for(int i=0;i<skip.length();i++){
            alp[skip.charAt(i)-'a']='-';
        }
        StringBuilder sb=new StringBuilder();
        for(int i=0;i<s.length();i++){
            int origin=s.charAt(i)-'a';
            int cnt=index;
            int idx=1;
            int changeIdx = 0;
            while(cnt>0){
                changeIdx=(origin+idx)%26;
                if(alp[changeIdx]!='-'){
                    idx++;
                    cnt--;
                    continue;
                }
                idx++;
            }
            sb.append(alp[changeIdx]);
        }
        return sb.toString();
    }
}

import java.util.*;
class Solution {
    public int solution(String[][] book_time) {
        int answer = 0;
        Arrays.sort(book_time,new Comparator<String[]>(){
            @Override
            public int compare(String[]s1,String[]s2){
                if(toSec(s1[1])<toSec(s2[1])){
                    return -1;
                }else if(toSec(s1[1])>toSec(s2[1])){
                    return 1;
                }else{
                    return toSec(s1[0])-toSec(s2[0]);
                }
            }
        });
        int n=book_time.length;
        for(int i=0;i<n;i++){
            System.out.println(book_time[i][0] +" "+book_time[i][1]);
        }
        boolean[] visit=new boolean[n];
       for (int i = 0; i < n; i++) {
            if (visit[i]) {
                continue;
            }
            visit[i] = true;
            String standard = book_time[i][1];
            answer++;
            for (int j = i + 1; j < n; j++) {
                if (!visit[j] && toSec(standard) + 10 <= toSec(book_time[j][0])) {
                    visit[j] = true;
                    standard = book_time[j][1];
                }
            }
        }
        
        return answer;
    }
    public int toSec(String s){
        String[]split=s.split(":");
        return Integer.parseInt(split[0])*60+Integer.parseInt(split[1]);
    }
}

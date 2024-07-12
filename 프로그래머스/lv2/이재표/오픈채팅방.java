import java.util.*;
class Solution {
    public String[] solution(String[] records) {
        Map<String,String>map=new HashMap<>();
        int cnt=0;
        for(int i=0;i<records.length;i++){
            String[] record=records[i].split(" ");
            if(record[0].equals("Change")){
                map.put(record[1],record[2]);
                continue;
            }
            if(record[0].equals("Enter")){
                map.put(record[1],record[2]);
            }
            cnt++;
        }
        String[] answer = new String[cnt];
        int idx=0;
        for(int i=0;i<records.length;i++){
            String[] record=records[i].split(" ");
            if(record[0].equals("Enter")){
                answer[idx++]=map.get(record[1])+"님이 들어왔습니다.";
            }else if(record[0].equals("Leave")){
                answer[idx++]=map.get(record[1])+"님이 나갔습니다.";
            }
        }
        return answer;
    }
}

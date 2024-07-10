import java.util.*;
class Solution {
    public String solution(int n, int t, int m, String[] timetable) {
        String answer = "";
        PriorityQueue<String> pq = new PriorityQueue<>(new Comparator<String>() {
            @Override
            public int compare(String s1, String s2) {
                String[] st1 = s1.split(":");
                String[] st2 = s2.split(":");
                if (Integer.valueOf(st1[0]).equals(Integer.valueOf(st2[0]))) {
                    return Integer.valueOf(st1[1]) - Integer.valueOf(st2[1]);
                } else {
                    return Integer.valueOf(st1[0]) - Integer.valueOf(st2[0]);
                }
            }
        });
        for(int i=0;i<timetable.length;i++){
            pq.offer(timetable[i]);
        }
        
        String time="09:00";
        Integer ct=calculateTime(time);
        int ride=0;
        String lastTime=pq.peek();
        for(int i=0;i<n;i++){
            ride=0;
            ct=calculateTime(time)+t*i;
            while(!pq.isEmpty()){
                Integer com=calculateTime(pq.peek());
                if(com<=ct && ride<m){
                    lastTime = pq.poll();
                    ride+=1;
                }else{
                    break;
                }
            }
        }
        
        if (ride < m) {
            answer = formatTime(calculateTime(time) + t * (n - 1));
        } else {
            answer = formatTime(calculateTime(lastTime) - 1);
        }

        return answer;
    }
    public String formatTime(int time) {
        int h = time / 60;
        int m = time % 60;
        return String.format("%02d:%02d", h, m);
    }
    public int calculateTime(String time) {
        String[] t = time.split(":");
        int h = Integer.parseInt(t[0]);
        int m = Integer.parseInt(t[1]);
        return h * 60 + m;
    }
}

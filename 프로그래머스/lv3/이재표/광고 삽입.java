import java.util.*;
class Solution {
    public int timeToSec(String time){
        String[]s=time.split(":");
        return Integer.parseInt(s[0])*3600+Integer.parseInt(s[1])*60+Integer.parseInt(s[2]);
    }
    public String secToTime(int time) {
        int H = time / 3600;
        int M = (time - 3600 * H) / 60;
        int S = time - 3600 * H - 60 * M;
        
        return (H < 10 ? "0" : "") + H + ":" +
            (M < 10 ? "0" : "") + M + ":" +
            (S < 10 ? "0" : "") + S;
    }
    public String solution(String play_time, String adv_time, String[] logs) {
        int playTime=timeToSec(play_time);
        int[]time=new int[360000];
         for (String log : logs) {
            String[] l = log.split("-");
            int start = timeToSec(l[0]);
            int end = timeToSec(l[1]);
            time[start] += 1;
            if (end <= playTime) {
                time[end] -= 1;
            }
        }

        for (int i = 1; i <= playTime; i++) {
            time[i] += time[i - 1];
        }
        
        long maxtotal=0;
        int adv=timeToSec(adv_time);
        for(int i=0;i<adv;i++){
            maxtotal+=time[i];
        }
        long total=maxtotal;
        int idx=0;
        for(int i=adv;i<playTime;i++){
            total=total+time[i]-time[i-adv];
            if(maxtotal<total){
                maxtotal=total;
                idx=i-adv+1;
            }
        }
        return secToTime(idx);
    }
}

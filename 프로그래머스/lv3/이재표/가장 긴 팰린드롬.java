import java.util.*;
class Solution{
    String sen;
    int answer=1;
    public int solution(String s){
        sen = s;
        for (int i = 0; i < s.length(); i++) {
            find(i, 1);
            find2(i, 0);
        }
        return answer;
    }
    public void find(int idx,int cnt){
        if (idx - cnt >= 0 && idx + cnt < sen.length()) {
            if (sen.charAt(idx - cnt) == sen.charAt(idx + cnt)) {
                if (answer < cnt * 2 + 1) {
                    answer = cnt * 2 + 1;
                }
                find(idx, cnt + 1);
            }
        }
    }
    public void find2(int idx, int cnt) {
        if (idx - cnt >= 0 && idx + cnt + 1 < sen.length()) {
            if (sen.charAt(idx - cnt) == sen.charAt(idx + cnt + 1)) {
                if (answer < (cnt + 1) * 2) {
                    answer = (cnt + 1) * 2;
                }
                find2(idx, cnt + 1);
            }
        }
    }
}

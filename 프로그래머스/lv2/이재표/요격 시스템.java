import java.util.*;
class Solution {
    public int solution(int[][] targets) {
        int answer = 0;
        Arrays.sort(targets, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                if (o1[1] != o2[1]) {
                    return o1[1] - o2[1];
                } else {
                    return o1[0] - o2[0];
                }
            }
        });
        int line=0;
        for(int i=0;i<targets.length;i++){
            if(line<=targets[i][0]){
                line=targets[i][1];
                answer++;
            }
        }
        return answer;
    }
}

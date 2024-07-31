import java.util.*;
class Solution {
    List<int[]>arr=new ArrayList<>();
    public int[][] solution(int n) {
        hanoi(n,1,2,3);
        int len = arr.size();
        int[][] answer = new int[len][2];
        for (int i = 0; i < len; i++) {
            int[] a = arr.get(i);
            answer[i][0] = a[0];
            answer[i][1] = a[1];
        }
        return answer;
    }
    private void hanoi(int cnt,int start,int mid,int end){
        if(cnt==0){
            return;
        }
        hanoi(cnt-1,start,end,mid);
        arr.add(new int[]{start,end});
        hanoi(cnt-1,mid,start,end);
    }
}

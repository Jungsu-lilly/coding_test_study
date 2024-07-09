// 1. 두 큐의 합을 구하고, 반을 나눠 target 값을 구함
// 2. 합이 홀수면 -1
// 3. 두 큐 값 비교해서 큰 쪽에서 하나씩 빼서 큰 쪽으로 옮김 (최대 이동 횟수)

import java.util.*;

class Solution {
    public int solution(int[] queue1, int[] queue2) {
        long q1Sum = 0L;
        Queue<Integer> q1 = new LinkedList<>();
        for (var e : queue1) { q1Sum += e; q1.add(e); }
        
        long q2Sum = 0L;
        Queue<Integer> q2 = new LinkedList<>();
        for (var e : queue2) { q2Sum += e; q2.add(e); }
        
        if ((q1Sum + q2Sum) % 2 != 0) return -1;
        
        int n = queue1.length * 2 + queue2.length;
        for (int i = 0; i <= n; ++i) {
            if (q1Sum == q2Sum) {
                return i;
            }
            if (q1Sum > q2Sum) {
                if (!q1.isEmpty()) {
                    int cur = q1.poll();
                    q2.add(cur);
                    q1Sum -= cur;
                    q2Sum += cur;
                }
            } else {
                if (!q2.isEmpty()) {
                    int cur = q2.poll();
                    q1.add(cur);
                    q2Sum -= cur;
                    q1Sum += cur; 
                }
            }
        }
        return -1;
    }
}

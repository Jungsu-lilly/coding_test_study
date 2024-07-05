import java.util.*;

class Solution {
    public int solution(int[] stones, int k) {
        int answer = Integer.MAX_VALUE;
        Deque<Integer> deque = new LinkedList<>();
        
        for (int i = 0; i < stones.length; i++) {
            while (!deque.isEmpty() && stones[deque.peekLast()] <= stones[i]) {
                deque.pollLast();
            }
            
            deque.addLast(i);
            
            if (deque.peekFirst() <= i - k) {
                deque.pollFirst();
            }
            
            if (i >= k - 1) {
                answer = Math.min(answer, stones[deque.peekFirst()]);
            }
        }
        
        return answer;
    }
}

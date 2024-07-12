import java.util.*;

// 트럭 현재 무게, 다리를 건너는데 걸리는 시간
// 1. 다리 하중보다 낮다면 현재 하중이 낮다면 계속 트럭 전진시킴
// 2. 다리를 건넌 트럭이 있다면 현재 하중에 트럭 무게 차감
// 3. 마지막으로 건넌 트럭이 다리를 건너는 데 걸리는 시간이 모든 트럭이 지나는데 걸리는 시간임

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {

        Queue<int[]> q = new LinkedList<>();
        int i = 0;
        int time = 0;
        int curWeight = 0;
        while (i < truck_weights.length) {
            if (curWeight + truck_weights[i] <= weight) {
                q.add(new int[]{truck_weights[i], time + bridge_length + 1});
                curWeight += truck_weights[i];
                ++i;
            }
            ++time;
            if (q.peek()[1] == time + 1) {
                curWeight -= q.poll()[0];
            }
        }
        int ans = 0;
        while (!q.isEmpty()) {
            ans = q.poll()[1];
        }
        return ans;
    }
}

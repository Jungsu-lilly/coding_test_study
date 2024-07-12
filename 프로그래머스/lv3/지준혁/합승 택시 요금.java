import java.util.*;

// 다익스트라 알고리즘
class Solution {

    List<int[]>[] adj = new ArrayList[204];

    public int solution(int n, int s, int a, int b, int[][] fares) {
        for (int i = 0; i <= n; ++i) adj[i] = new ArrayList<>();

        for (int i = 0; i < fares.length; ++i) {
            adj[fares[i][0]].add(new int[]{fares[i][2], fares[i][1]});
            adj[fares[i][1]].add(new int[]{fares[i][2], fares[i][0]});
        }

        int[] tgt = dijkstra(s, n);
        int ans = Integer.MAX_VALUE;
        for (int i = 1; i <= n; ++i) {
            int[] aln = dijkstra(i, n);
            int cost = tgt[i] + aln[a] + aln[b];
            ans = Math.min(ans, cost);
        }
        return ans;
    }

    int[] dijkstra(int st, int n) {
        int[] d = new int[n + 1];
        Arrays.fill(d, Integer.MAX_VALUE);
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        d[st] = 0;
        pq.add(new int[]{d[st], st});

        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int curWeight = cur[0];
            int curNode = cur[1];

            if (d[curNode] != curWeight) continue;

            for (var nxt : adj[curNode]) {
                int nxtWeight = nxt[0];
                int nxtNode = nxt[1];

                if (d[nxtNode] <= d[curNode] + nxtWeight) continue;
                d[nxtNode] = d[curNode] + nxtWeight;
                pq.add(new int[]{d[nxtNode], nxtNode});
            }
        }
        return d;
    }
}

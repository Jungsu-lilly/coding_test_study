import java.util.*;
class Solution {
    public int[] solution(int n, int[][] roads, int[] sources, int destination) {
        int[] answer = new int[sources.length];
        List<List<int[]>>graph=new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }
        for(int[]road:roads){
            graph.get(road[0]).add(new int[]{road[1],1});
            graph.get(road[1]).add(new int[]{road[0],1});
        }

        int[] dist = new int[n + 1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[destination] = 0;

        PriorityQueue<int[]> pq = new PriorityQueue<>(new Comparator<>(){
            @Override
            public int compare(int[]o1,int[]o2){
                return o1[1]-o2[1];
            }
        });
        pq.offer(new int[]{destination, 0});

       while (!pq.isEmpty()) {
            int[] current = pq.poll();
            int u = current[0];
            int d = current[1];

            if (d > dist[u]) {
                continue;
            }

            for (int[] g : graph.get(u)) {
                int v = g[0];
                int weight = g[1];

                if (dist[v] > dist[u] + weight) {
                    dist[v] = dist[u] + weight;
                    pq.offer(new int[]{v, dist[v]});
                }
            }
        }

        for (int i = 0; i < sources.length; i++) {
            answer[i] = (dist[sources[i]] == Integer.MAX_VALUE ? -1 : dist[sources[i]]);
        }

        return answer;
    }
}

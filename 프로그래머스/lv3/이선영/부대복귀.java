import java.util.*;

class Solution {
    public int[] solution(int n, int[][] roads, int[] sources, int destination) {
        int[] answer = new int[sources.length];
        int[] min = new int[n+1];
        List<Integer>[] list = new ArrayList[n+1];
        
        for(int i=0; i<list.length; i++){
            list[i] = new ArrayList<>();
        }
        
        for(int i=0; i<roads.length; i++){
            int[] road = roads[i];
            list[road[0]].add(road[1]);
            list[road[1]].add(road[0]);
        }
        
        boolean[] visited = new boolean[n+1];
        
        Arrays.fill(min, -1);

        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{destination, 0});
        
        
        while(!q.isEmpty()){
            int[] now = q.poll();
            if(visited[now[0]]) continue;
            
            visited[now[0]] = true;
            min[now[0]] = now[1];
            
            for(int j=0; j<list[now[0]].size(); j++){
                int next = list[now[0]].get(j);
                q.offer(new int[]{next, now[1]+1});
            }   
        }
        
        
        int tmp = 0;
        for(int i: sources){
            answer[tmp++] = min[i];
        }
        
        
        return answer;
    }
    
   
}

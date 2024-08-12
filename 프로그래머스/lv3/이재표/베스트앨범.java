import java.util.*;
class Solution {
    public int[] solution(String[] genres, int[] plays) {
        List<Integer>answer=new ArrayList<>();
        int idx=0;
        Map<String,Integer>map=new HashMap<>();
        for(int i=0;i<genres.length;i++){
            map.put(genres[i],map.getOrDefault(genres[i],0)+plays[i]);
        }
        List<String> keys = new ArrayList<>(map.keySet());

		Collections.sort(keys, (v1, v2) -> (map.get(v2).compareTo(map.get(v1))));
        
        for(String key:keys){
            List<int[]> songs = new ArrayList<>();
            for (int i = 0; i < genres.length; i++) {
                if (genres[i].equals(key)) {
                    songs.add(new int[]{i, plays[i]});
                }
            }  
            songs.sort((s1, s2) -> {
                if (s2[1] != s1[1]) {
                    return s2[1] - s1[1];
                } else {
                    return s1[0] - s2[0];
                }
            });
            
            for(int[] song:songs){
                System.out.println(song[0]);
            }
            int cnt=0;
            for(int[] song:songs){
                if(cnt==2){
                    break;
                }
                cnt++;
                answer.add(song[0]);
            }
        }
        return answer.stream().mapToInt(i->i).toArray();
    }
}

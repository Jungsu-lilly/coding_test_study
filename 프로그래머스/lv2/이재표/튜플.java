import java.util.*;
class Solution {
    public int[] solution(String s) {
        int[] answer;
        Map<String,Integer>map=new HashMap<>();
        for(int i=0;i<s.length();i++){
            if(s.charAt(i)=='{'){
                continue;
            }
            int idx=i;
            while((s.charAt(i)!=','&&s.charAt(i)!='}')){
                i++;
            }
            if(idx==i){
                continue;
            }
            String element=s.substring(idx,i);
            map.put(element,map.getOrDefault(element,0)+1);
        }
        List<String> list = new ArrayList<>(map.keySet());
        Collections.sort(list,new Comparator<String>(){
            @Override
            public int compare(String s1,String s2){
                return map.get(s2)-map.get(s1);
            }
        });
        answer=new int[list.size()];
        for(int i=0;i<list.size();i++){
            answer[i]=Integer.parseInt(list.get(i));
        }
        return answer;
    }
}

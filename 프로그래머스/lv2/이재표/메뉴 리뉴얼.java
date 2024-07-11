import java.util.*;
class Solution {
    Map<String,Integer>map=new HashMap<>();
    public String[] solution(String[] orders, int[] course) {
        String[] answer = {};
        for(int j=0;j<course.length;j++){
            for(int i=0;i<orders.length;i++){
                boolean[]visit=new boolean[orders[i].length()];
                combination(orders[i],visit,0,0,course[j]);
            }    
        }
        for(String key:map.keySet()){
            System.out.println("key : "+key+" value : "+map.get(key));
        }
        return answer;
    }
    public void combination(String arr,boolean[] visit,int start,int depth,int r){
       if(depth==r){
           String com="";
           for(int i=0;i<arr.length();i++){
               if(visit[i]==true){
                   com+=arr.charAt(i);
               }
           }
           map.put(com.toString(), map.getOrDefault(com, 0) + 1);
           return;
       } 
        for(int i=start;i<arr.length();i++){
            if(!visit[i]){
                visit[i]=true;
                combination(arr,visit,i+1,depth+1,r);
                visit[i]=false;
            }
        }
    } 
}

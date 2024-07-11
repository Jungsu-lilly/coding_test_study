import java.util.*;
class Solution {
    public int[] solution(String[] gems) {
        int[] answer = {};
        Map<String,Integer>map=new HashMap<>();
        for(int i=0;i<gems.length;i++){
            map.put(gems[i],map.getOrDefault(gems[i],0)+1);
        }
        
        
        int start1 = 0;
        int end1 = gems.length - 1; 
        for (; start1 < gems.length; start1++) {
            int n = map.get(gems[start1]);
            if (n - 1 > 0) {
                n--;
                map.put(gems[start1], n);
            } else {
                break;
            }
        }
        for (; end1 > start1; end1--) {
            int n = map.get(gems[end1]);
            if (n - 1 > 0) {
                n--;
                map.put(gems[end1], n);
            } else {
                break;
            }
        }
        
        
        
        int start2 = 0;
        int end2 = gems.length - 1; 
        for (; start2 < gems.length; start2++) {
            int n = map.get(gems[start2]);
            if (n - 1 > 0) {
                n--;
                map.put(gems[start2], n);
            } else {
                break;
            }
        }
        for (; end2 > start2; end2--) {
            int n = map.get(gems[end2]);
            if (n - 1 > 0) {
                n--;
                map.put(gems[end2], n);
            } else {
                break;
            }
        }
        
        if(end2-start2>end1-start1){
            return new int[]{start1,end1};    
        }else{
            return new int[]{start2,end2};
        }
        
    }
}

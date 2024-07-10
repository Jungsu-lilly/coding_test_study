import java.util.*;

class Solution {
    
    Map<String, Integer> map = new HashMap<>();
    
    public String[] solution(String[] orders, int[] course) {
        
        List<Map.Entry<String, Integer>> menu = new ArrayList<>();
        
        for (int i = 0; i < course.length; ++i) {
            for (int j = 0; j < orders.length; ++j) {
                char[] chars = orders[j].toCharArray();
                Arrays.sort(chars);
                dfs(new StringBuilder(), course[i], 0, chars);
            }
            int maxValue = 1;
            for (var e : map.entrySet()) {
                if (e.getValue() > maxValue) {
                    maxValue = e.getValue();
                }
            }

            if (maxValue != 1) {
                for (var e : map.entrySet()) {
                    if (e.getValue() == maxValue) {
                        menu.add(e);
                    }
                }
            }
            map.clear();
        }
        
        menu.sort((e1, e2) -> {
            return e1.getKey().compareTo(e2.getKey());
        });
        
        List<String> ans = new ArrayList<>();
        for (var e : menu) {
            ans.add(e.getKey());
        }
     
        return ans.toArray(new String[0]);
    }
    
    void dfs(StringBuilder sb, int digit, int st, char[] chars) {
        if (sb.length() == digit) {
            map.put(sb.toString(), map.getOrDefault(sb.toString(), 0) + 1);
            return;
        }
        
        for (int i = st; i < chars.length; ++i) {
            sb.append(chars[i]);
            dfs(sb, digit, i + 1, chars);
            sb.deleteCharAt(sb.length() - 1);
        }
    }
}

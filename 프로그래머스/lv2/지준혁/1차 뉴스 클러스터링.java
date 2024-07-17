import java.util.*;

class Solution {
    public int solution(String str1, String str2) {
        
        str1 = str1.toLowerCase();
        str2 = str2.toLowerCase();
        
        Map<String, Integer> m1 = createMultiSet(str1.toCharArray());
        Map<String, Integer> m2 = createMultiSet(str2.toCharArray());
        
        if (m1.size() == 0 && m2.size() == 0)
            return 65536;
        
        int a = findInter(m1, m2);
        int b = findUnion(m1, m2);
        
        double jakad = (double) a / b;
        
        return (int)(65536 * jakad);
    }
    
    Map<String, Integer> createMultiSet(char[] chars) {
        
        Map<String, Integer> m = new HashMap<>();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < chars.length - 1; ++i) {
            sb.setLength(0);
            if (chars[i] >= 'a' && chars[i] <= 'z' && chars[i + 1] >= 'a' && chars[i + 1] <= 'z') {
                sb.append(chars[i]);
                sb.append(chars[i + 1]);
                m.put(sb.toString(), m.getOrDefault(sb.toString(), 0) + 1);
            }
        }
        
        return m;
    }
    
    int findInter(Map<String, Integer> m1, Map<String, Integer> m2) {
        
        int ret = 0;
        for (var key : m1.keySet()) {
            if (m2.containsKey(key)) {
                ret += Math.min(m1.get(key), m2.get(key));
            }
        }
        return ret;
    }
    
    int findUnion(Map<String, Integer> m1, Map<String, Integer> m2) {
        
        int ret = 0;
        for (var key : m1.keySet()) {
            if (m2.containsKey(key)) {
                ret += Math.max(m1.get(key), m2.get(key));
            } else {
                ret += m1.get(key);
            }
        }
        for (var key : m2.keySet()) {
            if (!m1.containsKey(key)) {
                ret += m2.get(key);
            }
        }
        return ret;
    } 
}

import java.util.*;

class Solution {
    
    int nxtKey = 27;
    public int[] solution(String msg) {
        
        Map<String, Integer> m = initDict();
        
        int i = 0;
        int len = msg.length();
        List<Integer> ret = new ArrayList<>();
        while (i < len) {
            i += findAndAddDict(i, len, msg, m, ret);
        }
           
        int[] ans = new int[ret.size()];
        for (i = 0; i < ret.size(); ++i) {
            ans[i] = ret.get(i);
        }
        return ans;
    }
    
    Map<String, Integer> initDict() {
        
        char alpha = 'A';
        Map<String, Integer> m = new HashMap<>();
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= 26; ++i) {
            sb.setLength(0);
            sb.append(alpha);
            m.put(sb.toString(), i);
            ++alpha;
        }
        return m;
    }
    
    int findAndAddDict(int st, int len, String msg, Map<String, Integer> m, List<Integer> ret) {
        
        StringBuilder sb = new StringBuilder();
        for (int i = len ; i >= st; --i) {
            String word = msg.substring(st, i);
            if (m.containsKey(word)) {
                sb.setLength(0);
                sb.append(word);
                if (i != len) { 
                    sb.append(msg.charAt(i));
                    m.put(sb.toString(), nxtKey++);
                }
                ret.add(m.get(word));
                return word.length();
            }
        }
        
        return 1;
    }
}

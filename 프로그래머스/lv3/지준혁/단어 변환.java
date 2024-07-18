import java.util.*;

class Solution {
    public int solution(String begin, String target, String[] words) {
        
        Set<String> wordSet = new HashSet<>(Arrays.asList(words));
        Queue<String> q = new LinkedList<>();
        Set<String> isVisited = new HashSet<>();
        
        isVisited.add(begin);
        q.add(begin);
        
        int ans = 0;
        while (!q.isEmpty()) {
            
            for (int i = 0; i < q.size(); ++i) {
                String cur = q.poll();
                
                if (cur.equals(target)) {
                    return ans;
                }
                
                for (var nxt : getNxtWords(cur, wordSet)) {
                    if (!isVisited.contains(nxt)) {
                        isVisited.add(nxt);
                        q.add(nxt);
                    }
                }
            }
            ++ans;
        }
        return 0;
    }
    
    List<String> getNxtWords(String word, Set<String> wordSet) {
        
        List<String> ret = new ArrayList<>();
        char[] chars = word.toCharArray();
        
        for (int i = 0; i < chars.length; ++i) {
            char cur = chars[i];
            for (char c = 'a'; c <= 'z'; ++c) {
                if (c == cur) continue;
                chars[i] = c;
                String nxt = new String(chars);
                if (wordSet.contains(nxt)) {
                    ret.add(nxt);
                }
            }
            chars[i] = cur;
        }
        return ret;
    }
}

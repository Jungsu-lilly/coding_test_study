import java.util.*;

class Solution {
    
    List<String> ans = new ArrayList<>();
    
    public String solution(String p) {
        
        String ans = convert(p);
        return ans;
    }
    
    boolean isCorrect(String p) {
        Stack<Character> s = new Stack<>();
        
        for (var e : p.toCharArray()) {
            if (e == '(') s.push(e);
            else if (e == ')') {
                if (s.isEmpty() || s.peek() != '(') return false;
                s.pop();
            }
        }
        if (!s.isEmpty()) return false;
        
        return true;
    }
    
    int startBalancedIdx(String p) {
        int ocnt = 0;
        int ccnt = 0;
        
        char[] chars = p.toCharArray();
        for (int i = 0; i < chars.length; ++i) {
            if (chars[i] == '(') ++ocnt;
            else if (chars[i] == ')') ++ccnt;
            
            if (ocnt == ccnt) return i;
        }
        return -1;
    }
    
    String eraseAndReverse(String p) {
        
        StringBuilder sb = new StringBuilder();
        
        char[] chars = p.toCharArray();
        for (int i = 0; i < chars.length; ++i) {
            if (i == 0 || i == chars.length - 1) continue;
            
            if (chars[i] == '(') sb.append(')');
            else if (chars[i] == ')') sb.append('(');
        }
        return sb.toString();
    }
    
    String convert(String p) {
        
        if (p.isEmpty()) return p;
        
        int bIdx = startBalancedIdx(p);
        String u = p.substring(0, bIdx + 1);
        String v = p.substring(bIdx + 1);
        
        StringBuilder sb = new StringBuilder(); 
        if (isCorrect(u)) {
            sb.append(u);
            sb.append(convert(v));
        } else {
            sb.append('(');
            sb.append(convert(v));
            sb.append(')');
            sb.append(eraseAndReverse(u));
        }
        return sb.toString();
    }
}

import java.util.*;
class Solution {
    public String solution(String p) {
        return dfs(p);
    }
     public String dfs(String p) {
        if (p.length() == 0) {
            return "";
        }

        String u = "";
        String v = "";

        int u1 = 0, u2 = 0;
        int li = 0;
        for (int i = 0; i < p.length(); i++) {
            if (p.charAt(i) == '(') {
                u1++;
            } else {
                u2++;
            }
            if (u1 == u2) {
                li = i;
                break;
            }
        }
        u = p.substring(0, li + 1);
        v = p.substring(li + 1);
        if (rightBlank(u)) {
            return u + dfs(v);
        } else {
            return "(" + dfs(v) + ")" + reverse(u.substring(1, u.length() - 1));
        }
    }
    public String reverse(String sen) {
        StringBuilder answer = new StringBuilder();
        for (int i = 0; i < sen.length(); i++) {
            if (sen.charAt(i) == '(') {
                answer.append(')');
            } else {
                answer.append('(');
            }
        }
        return answer.toString();
    }

    public boolean rightBlank(String sentences) {
        Stack<Character> stack = new Stack<>();
        for (Character sen : sentences.toCharArray()) {
            if (!stack.isEmpty() && stack.peek() == '(' && sen == ')') {
                stack.pop();
            } else {
                stack.push(sen);
            }
        }
        return stack.isEmpty();
    }
}

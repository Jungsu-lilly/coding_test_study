import java.util.*;

class Solution {
    public int[] solution(String s) {

        s = s.substring(2, s.length() - 2);
        String[] tuples = s.split("\\},\\{");
        Arrays.sort(tuples, (a, b) -> Integer.compare(a.length(), b.length()));
        
        Set<Integer> checker = new HashSet<>();
        List<Integer> ret = new ArrayList<>();
        
        for (var tuple : tuples) {
            String[] nums = tuple.split(",");
            for (var num : nums) {
                int e = Integer.parseInt(num);
                if (checker.add(e)) ret.add(e);
            }
        }

        int[] ans = new int[ret.size()];
        for (int i = 0; i < ret.size(); ++i) {
            ans[i] = ret.get(i);
        }
        return ans;
    }
}

import java.util.*;
class Solution {
    public int[] solution(String[] enroll, String[] referral, String[] seller, int[] amount) {
        int n = enroll.length;
        int[] answer = new int[n];
        Map<String, Integer> map = new HashMap<>();

        for (int i = 0; i < n; i++) {
            map.put(enroll[i], i);
        }

        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            if (referral[i].equals("-")) {
                arr[i] = -1;
            } else {
                arr[i] = map.get(referral[i]);
            }
        }

        for (int i = 0; i < seller.length; i++) {
            int sellerIndex = map.get(seller[i]);
            int p = sellerIndex;
            int totalAmount = amount[i] * 100;

            while (p != -1) {
                int up = totalAmount / 10;
                answer[p] += totalAmount - up;
                totalAmount = up;
                p = arr[p];
                if (totalAmount == 0) {break};
            }
        }

        return answer;
    }

}
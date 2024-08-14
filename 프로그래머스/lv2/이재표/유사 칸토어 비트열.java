import java.util.*;
class Solution {
    public int solution(int n, long l, long r) {
        return countOnes(n, l, r);
    }

    private int countOnes(int n, long l, long r) {
        if (n == 0) {
            return l <= 1 && 1 <= r ? 1 : 0;
        }
        long segmentLength = (long) Math.pow(5, n - 1);
        int totalOnes = 0;
        for (long i = l; i <= r; i++) {
            totalOnes += getValue(n, i, segmentLength);
        }
        return totalOnes;
    }

    private int getValue(int n, long index, long segmentLength) {
        if (n == 0) {
            return 1;
        }
        long position = (index - 1) / segmentLength % 5;
        if (position == 2) { 
            return 0;
        }
        return getValue(n - 1, index, segmentLength / 5);
    }
}

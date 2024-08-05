import java.util.*;
class Solution {
    public int[] solution(long begin, long end) {
        int size=(int)(end - begin + 1);
        int[]answer=new int[size];
        Arrays.fill(answer,0);
        int idx=0;
        for(long i=begin;i<=end;i++){
            answer[idx++]=(int)findMax(i);
        }
        return answer;
    }
    public long findMax(long begin) {
        if (begin <= 1) {
            return 0; 
        }
        
        long maxDivisor = 1; 
        
        for (long i = 2; i * i <= begin; i++) {
            if (begin % i == 0) {
                long divisor1 = i;
                long divisor2 = begin / i;

                  if (divisor1 != begin && divisor1 > maxDivisor && divisor1 <= 10000000) {
                    maxDivisor = divisor1;
                }
                if (divisor2 != begin && divisor2 > maxDivisor && divisor2 <= 10000000) {
                    maxDivisor = divisor2;
                }
            }
        }

        return maxDivisor;
    }
}

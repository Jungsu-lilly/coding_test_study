import java.util.*;
class Solution {
    public int solution(int n) {
        int answer = 0;
        if(n%2!=0){
            return 0;
        }
        long[]dp=new long[5001];
        dp[0]=1;
        dp[1]=0;
        dp[2]=3;
        for(int i=4;i<=n;i++){
            dp[i]=dp[i-2]*3;
            for(int j=i-4;j>=0;j-=2){
                dp[i]+=2*dp[j];
            }
            dp[i]=dp[i]%1000000007;
        }
        return (int)dp[n];
    }
}

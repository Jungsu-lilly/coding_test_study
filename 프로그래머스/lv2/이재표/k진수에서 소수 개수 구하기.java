import java.util.*;
class Solution {
    public int solution(int n, int k) {
        int answer = 0;
        String num=Integer.toString(n,k);
        int len=num.length();
        for(int i=0;i<len;){
            int start=i;
            int end=i;
            while(end<len&&num.charAt(end)!='0'){
                end++;
            }
            if(isPrime(num.substring(start,end))){
                answer++;
            }
             while(end<len&&num.charAt(end)=='0'){
                end++;
            }
            i=end;
        }
        return answer;
    }
    public boolean isPrime(String num){
        Integer n=Integer.valueOf(num);
        boolean prime[]=new boolean[n+1];
        prime[0]=prime[1]=true;
        for(int i=2;i*i<=n;i++){
            if(!prime[i]){
                for(int j=i*2;j<=n;j+=i){
                    prime[j]=true;
                }
            }
        }
        return !prime[n];
    }
}

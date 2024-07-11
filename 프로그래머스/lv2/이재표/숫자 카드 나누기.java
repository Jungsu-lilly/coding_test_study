import java.util.*;
class Solution {
    private int gcd(int[]arr){
        int result=arr[0];
        for(int i=1;i<arr.length;i++){
            result=gcd(result,arr[i]);
        }
        return result;
    }
    private int gcd(int a,int b){
        if(b==0){
            return a;
        }
        return gcd(b,a%b);
    }
    public boolean verify(int target,int[]arr){
        int cnt=0;
        for(int i=0;i<arr.length;i++){
            if(arr[i]%target==0){
                cnt++;
            }
        }
        if(cnt>0){
            return false;
        }else{
            return true;
        }
    }
    public int solution(int[] arrayA, int[] arrayB) {
        int A = gcd(arrayA);
        boolean AtoB=verify(A,arrayB);
        System.out.println(AtoB);

        int B = gcd(arrayB);
        boolean BtoA=verify(B,arrayA);
        System.out.println(BtoA);

        if(AtoB && !BtoA){
            return A;
        }else if(!AtoB && BtoA){
            return B;
        }else if(AtoB && BtoA){
            return Math.max(A,B);
        }else{
            return 0;
        }

    }
}
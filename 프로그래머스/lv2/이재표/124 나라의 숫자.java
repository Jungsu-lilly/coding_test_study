import  java.util.*;
class Solution {
    public String solution(int n) {
        String[] numbers = {"4", "1", "2"};
        String answer = "";
      
        int num = n;

        while(num > 0){
            int rear = num % 3;
            num /= 3;

            if(rear == 0) {
                num--;
            }

            answer = numbers[rear] + answer;
        }

        return answer;
    }
}

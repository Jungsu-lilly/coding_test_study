#include <string>
#include <vector>
#include <iostream>
#include <string>
using namespace std;

string solution(int n) {
    string answer = "";
    
    while(n>0){
        
        int remain = n % 3;
        n = n / 3 ;
        
        if(remain == 0){
            answer = "4" + answer;
            n--;
            
        }else{
            answer = to_string(remain) + answer;
        }
        
    }
    
    return answer;
}

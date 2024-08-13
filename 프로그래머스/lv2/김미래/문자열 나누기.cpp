#include <string>
#include <vector>
#include <iostream>
using namespace std;

int solution(string s) {
    int answer = 0;
    char now =s[0];
    int nowCount = 0;
    int anotherCount = 0;
    
    for(int i=0; i<s.length(); i++){
        if(now == s[i]){
            nowCount++;
        }else{
            anotherCount++;
        }
        
        if(nowCount == anotherCount){
            answer++;
            if(i<s.length()-1){
                now = s[i+1];
                nowCount = 0; 
                anotherCount = 0; 
            }
        }    
        if(nowCount != anotherCount && i==s.length()-1){
            answer++;
        }
    }
    
    return answer;
}

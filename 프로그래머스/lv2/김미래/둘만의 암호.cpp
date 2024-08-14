#include <string>
#include <vector>
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string solution(string s, string skip, int index) {
    string answer = "";
    for(int i=0; i<s.length(); i++){
        
        char now = s[i];
        int count = 0;
        
        while(count<index){
            now++;
            if(now > 'z'){
                now = 'a';
            }
        
            if (skip.find(now) == string::npos) {  
                count++;
            }
            
        }
         answer += now;
        
    }
    return answer;
}

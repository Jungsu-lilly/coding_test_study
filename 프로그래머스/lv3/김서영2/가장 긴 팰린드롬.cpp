#include <iostream>
#include <string>
using namespace std;
string palindrome(string s, int left, int right) {
    while(left >= 0 && right < s.length() && s[left] == s[right]) {
        left--;
        right++;
    }
    return s.substr(left+1, right-left-1);
}
int solution(string s)
{
    int answer=0;
    for(int i=0; i<s.length(); i++) {
        // 중심이 홀수일때
        string odd = palindrome(s,i,i);
        if(odd.length() > answer) answer = odd.length();
        
        // 중심이 짝수일때
        string even = palindrome(s,i,i+1);
        if(even.length() > answer) answer = even.length();
    }

    return answer;
}
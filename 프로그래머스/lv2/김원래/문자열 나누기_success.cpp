#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(string s) {
    int answer = 0;
    
    char compare = ' ';
    int cnt1 = 0;
    int cnt2 = 0;
    
    for(int idx = 0 ; idx < s.size() ; ++idx)
    {
        if(compare == ' ')
        {
            ++cnt1;
            compare = s[idx];
        }
        else if(compare == s[idx]) ++cnt1;
        else
        {
            ++cnt2;
            if(cnt1 == cnt2)
            {
                ++answer;
                compare = ' ';
                cnt1 = 0;
                cnt2 = 0;
            }
        }

    }
    if(cnt1 > 0) ++answer;
    
    return answer;
}
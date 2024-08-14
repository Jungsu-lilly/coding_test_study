#include <string>
#include <vector>

using namespace std;

char _skip[26];

string solution(string s, string skip, int index) {
    string answer = "";
    
    for(int cnt = 0 ; cnt < skip.size() ; ++cnt)
    {
        int idx = skip[cnt] % 'a';
        _skip[idx] = 1;
    }
    

    for(int cnt = 0 ; cnt < s.size() ; ++cnt)
    {
        int checkIdx = s[cnt] % 'a';
        
        for(int _index = 1 ; _index <= index ; ++_index)
        {
            checkIdx = (checkIdx + 1) % 26;
            while(_skip[checkIdx] == 1) checkIdx = (checkIdx + 1) % 26;
        }
        
        answer.push_back(checkIdx + 'a');
    }
    
    return answer;
}

/*


넘어가는 것을 생각해서 모듈러 연산 + 남은걸 더하는 방식으로 간다?
배열로 만들어서 skip을 표시한다.


*/
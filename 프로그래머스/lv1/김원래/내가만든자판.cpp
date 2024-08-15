#include <string>
#include <vector>

using namespace std;

const int INVALID_KEY = 101;

int keyCnts[26];

vector<int> solution(vector<string> keymap, vector<string> targets) {
    vector<int> answer;
    
    
    for(int cnt = 0 ; cnt < 26 ; ++cnt)
    {
        keyCnts[cnt] = INVALID_KEY;
    }
    
    for(int cnt = 0 ; cnt < keymap.size() ; ++cnt)
    {
        for(int ch = 0 ; ch < keymap[cnt].size() ; ++ch)
        {
            keyCnts[keymap[cnt][ch] - 'A'] = min(keyCnts[keymap[cnt][ch] - 'A'], ch + 1);
        }
    }
    
    for(int cnt = 0 ; cnt < targets.size() ; ++cnt)
    {
        int  totalCnt = 0;
        bool invalidFlag = false;
        for(int ch = 0 ; ch < targets[cnt].size() ; ++ch)
        {
            int curCnt = keyCnts[targets[cnt][ch] - 'A'];
            
            if(curCnt == INVALID_KEY)
            {
                invalidFlag = true;
                break;
            }
            
            totalCnt += curCnt;
        }
        if(invalidFlag == true) answer.push_back(-1);
        else answer.push_back(totalCnt);
    
    }
    
    return answer;
}
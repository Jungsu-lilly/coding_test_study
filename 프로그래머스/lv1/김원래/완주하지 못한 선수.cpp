#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

unordered_map<string, int> uMap;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    
    for(int cnt = 0 ; cnt  < completion.size() ; ++cnt)
    {
        if(uMap.find(completion[cnt]) == uMap.end())
            uMap.insert({completion[cnt], 1});
        else
            uMap[completion[cnt]]++;
    }
    
    for(int cnt = 0 ; cnt < participant.size() ; ++cnt)
    {
        if(uMap.find(participant[cnt]) == uMap.end())
        {
            answer = participant[cnt];
            break;
        }
        
        if(uMap[participant[cnt]]-- == 0)
        {
            answer = participant[cnt];
            break;
        }
        
    }
    
    return answer;
}
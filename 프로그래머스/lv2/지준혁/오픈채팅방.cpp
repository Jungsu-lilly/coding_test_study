#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>
#include <sstream>

using namespace std;

vector<string> solution(vector<string> record) {
    
    unordered_map<string, string> map;
    
    for (auto e : record) {
        istringstream iss(e);
        vector<string> split;
        string tmp;
        while (getline(iss, tmp, ' ')) 
            split.push_back(tmp);
        if (split[0] == "Enter" || split[0] == "Change") {
            map[split[1]] = split[2];
        }
    }
    vector<string> ans;
    for (auto& e: record) {
        string ret = "";
        istringstream iss(e);
        vector<string> split;
        string tmp;
        while (getline(iss, tmp, ' ')) 
            split.push_back(tmp);
        
        if (split[0] == "Enter") {
            ret += map[split[1]];
            ret += "님이 들어왔습니다.";
            ans.push_back(ret);
        }
        else if (split[0] == "Leave") {
            ret += map[split[1]];
            ret += "님이 나갔습니다.";
            ans.push_back(ret);
        }
    }

    return ans;
}

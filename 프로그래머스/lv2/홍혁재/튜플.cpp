// "{{1,2}, {2}}" => [[2,1], [2]]
// 길이 기준 오름차순으로 정렬 => [[2], [2,1]]
// 각 원소를 탐색하며 set에 추가 <- 중복되지 않게 순서대로

#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <set>

using namespace std;

bool compare(vector<int> x, vector<int> y) {
    return x.size() < y.size();
}

vector<int> solution(string s) {
    vector<int> answer;
    string token, token2;
    vector<string> b;
    vector<vector<int>> splited;
    
        
    
    // "{{2}, {2,1}}" => [[2], [2,1]] -> splited
    string a = s.substr(1, s.length() - 2);
    a = ',' + a;
    stringstream ss(a);
    
    while(getline(ss, token, '{')) {
        splited.push_back(vector<int>());
        token = token.substr(0,2);
        stringstream ss2(token);
        while(getline(ss2, token2, ',')) {
            splited.back().push_back(stoi(token2));
        }
    }

    sort(splited.begin(), splited.end(), compare);
    
    set<int> answerSet;
    
    for(int i = 1; i <= splited.size(); i++) {
        for(int j = 0; j <= splited[i].size(); j++) {
            answerSet.insert(splited[i][j]);
        }
    }
  return answer;
}
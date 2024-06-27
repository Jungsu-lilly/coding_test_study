#include <string>
#include <vector>
#include <iostream>

using namespace std;

string solution(int n, int k, vector<string> cmd) {
    
    vector<int> v;
    vector<pair<int, int>> h;
    for (int i = 0; i < n; ++i) {
        v.push_back(i);
    }
    
    int cursor = k;
    for (auto c : cmd) {
        if (c[0] == 'U') {

            cursor -= c[2]; //atoi
        }
        else if (c[0] == 'D') {

            cursor += c[2]; 
        }
        else if (c[0] == 'C') {
            pair<int, int> removed = {cursor, v[cursor]};
            v.erase(v.begin() + cursor);
            h.push_back(removed);
        }
        else if (c[0] == 'Z') {
            v.insert(v.begin() + h[0].first, h[1].second);
            h.erase(h.begin());
        }
    }
    return "OX";
}

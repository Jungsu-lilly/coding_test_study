#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <iterator>
#include <list>

using namespace std;

list<int> l;
list<int>::iterator l_it[1000004];
list<int>::iterator cursor; 
stack<pair<int,int>> s;
string solution(int n, int k, vector<string> cmd) {
    
    for(int i = 0; i < n; i++)
        l.push_back(i);
    auto it = l.begin();
    for(int i = 0; i < n; i++) {
        l_it[i] = it;
        it++;        
    }

    cursor = l_it[k];
    
    for (auto str : cmd) {
        if (str[0] == 'U') {
            int num = stoi(str.substr(2));
            while(num--) --cursor;
        }
        else if (str[0] == 'D') {
            int num = stoi(str.substr(2));
            while(num--) ++cursor;
        }
        else if (str[0] == 'C') {
            auto init = cursor;
            cursor = l.erase(cursor); 
            if (cursor == l.end()) {
                --cursor;
            }
            s.push({ *init, *cursor });
        }
        else {
            auto [cur, nxt] = s.top(); s.pop();
                        
            if (cur < nxt) {
                l.insert(l_it[nxt], cur);
                auto tmp = l_it[nxt];
                tmp--;
                l_it[cur] = tmp;
            }
            else {
                l.insert(l.end(), cur);
                l_it[cur] = --l.end();
            }
        }        
    }
    string str(n, 'X');
    for (auto e : l) {
        str[e] = 'O';
    }

    return str;
}

#include <string>
#include <vector>
#include <stack>
#include <iostream>

using namespace std;

bool is_correct(string& str) {
    stack<char> s;
    
    for (auto& c : str) {
        if (c == '(' || c == '[' || c == '{') {
            s.push(c);
        }
        else if (c == ')') {
            if (!s.empty() && s.top() == '(') {
                s.pop();
            } else {
                return false;
            }
        }
        else if (c == ']') {
            if (!s.empty() && s.top() == '[') {
                s.pop();
            } else {
                return false;
            }
        }
        else if (c == '}') {
            if (!s.empty() && s.top() == '{') {
                s.pop();
            } else {
                return false;
            }
        }
    }
    if (!s.empty()) {
        return false;
    }
    return true;
}

int solution(string s) {
    int ans = 0;
    int len = s.length();
    for (int i = 0; i < len; ++i) {
        if (is_correct(s)) {
            ++ans;
        }   
        s.push_back(s[0]);
        s.erase(0, 1);
    }
    return ans;
}

#include <string>
#include <vector>

using namespace std;

bool check(string u) {
    vector<char> stk;
    while(!u.empty()) {
       if(u[0] == '(') {
           stk.push_back(u[0]);
           u.erase(0,1);
       } 
        else {
            u.erase(0,1);
            if(stk.empty()) {
                return false;
            }
            stk.pop_back();
        }
    }
    if(!stk.empty()) return false;
    return true;
}

string recursion(string u, string v, int cnt) {
    if(u.empty() && v.empty()) return "";
    while(!v.empty()) {
        if(u != "" && cnt == 0){
            if(check(u)) u += recursion("", v, 0);
            else {
                string a = '(' + recursion("", v, 0) + ')';
                u.erase(0,1);
                u.erase(u.length() - 1, 1);
                for(int i = 0; i < u.length(); i++){
                    u[i] = (u[i] == ')') ? '(' : ')';
                }
                return a + u;
            }
        } 
        if(v[0] == '(') ++cnt;
        else --cnt;
        u += v[0];
        v.erase(0,1);
    }
    if(check(u)) return recursion("", v, 0);
    else {
        string a = '(' + recursion("", v, 0); + ')';
        u.erase(0,1);
        u.erase(u.length() - 1, 1);
        for(int i = 0; i < u.length(); i++) {
            u[i] = (u[i] == ')') ? '(' : ')';
        }
        return a + u;
    }
    return u;
}

string solution(string p) {
    string answer = "";
    if(check(p)) return p;
   	answer = recursion("", p, 0); 
    return answer;
}
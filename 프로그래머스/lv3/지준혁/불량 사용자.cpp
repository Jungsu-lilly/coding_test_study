#include <string>
#include <vector>
#include <unordered_set>
#include <iostream>

using namespace std;

// 1. banned_id를 순회하며 가능한 id를 set 배열에 담는다.
// 2. set 각 배열에서 원소를 하나씩 골라 가능한 경우를 vector에 담는다. vector에 하나씩 옮겨 담을 때 현재 담은 원소를 제외한 원소를 담을 수 없다면 건너뛴다.
// 3. vector 배열에 있는 원소를 순회하며, 하나라도 ret(set)에 없다면 담는다. (개수를 센다)

unordered_set<string> s[8];
unordered_set<string> ret;

bool is_banned_id(string ban, string user) {
    int idx = 0;
    
    if (ban.length() != user.length())
        return false;
    
    while (ban[idx]) {
        if (ban[idx] == '*') {
            ++idx;
            continue;
        }
        if (ban[idx] == user[idx])
            ++idx;
        else {
            return false;
        }
    }
    return true;
}

int solution(vector<string> user_id, vector<string> banned_id) {
    
    for (int i = 0; i < banned_id.size(); ++i) {
        string banned = banned_id[i];
        for (int j = 0; j < user_id.size(); ++j) {
            if (is_banned_id(banned, user_id[j])) {
                s[i].insert(user_id[j]);
            }
        }
    }
    int n = banned_id.size();
    for (int i = 0; i < n; ++i) {
        for (auto e : s[i])
            cout << "e: " << e << ' ';
        cout << '\n';
    }
    int answer = 0;
    return answer;
}

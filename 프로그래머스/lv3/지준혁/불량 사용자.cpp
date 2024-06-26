#include <string>
#include <vector>
#include <unordered_set>
#include <set>
#include <iostream>

using namespace std;

vector<string> s[8];
int ans = 0;

// 1. banned_id를 순회하며 가능한 id를 s배열에 저장한다.
// 2. dfs로 s배열에서 하나씩 골라 가능한 순열을 만든다. 
// 3. 해당 순열을 전체를 저장할 수 있도록 set<set<string>> ret에 저장한다.
// 4. 중복 순열이 제거되므로 ret size가 답이다.

bool is_banned_id(string ban, string user) {

    if (ban.length() != user.length())
        return false;

    int idx = -1;
    while (ban[++idx]) {
        if (ban[idx] == '*') {
            continue;
        }
        if (ban[idx] != user[idx])
            return false;
    }
    return true;
}


void dfs(int depth, int n, set<string>& seq, set<set<string>>& ret) {

    if (depth == n) {
        ret.insert(seq);
        return ;
    }
    for (auto e : s[depth]) {
        if (seq.find(e) == seq.end()) {
            seq.insert(e);
            dfs(depth + 1, n, seq, ret);
            seq.erase(e);
        }
    }
}

int solution(vector<string> user_id, vector<string> banned_id) {

    for (int i = 0; i < banned_id.size(); ++i) {
        string banned = banned_id[i];
        for (int j = 0; j < user_id.size(); ++j) {
            if (is_banned_id(banned, user_id[j])) {
                s[i].push_back(user_id[j]);
            }
        }
    }

    int n = banned_id.size();
    set<string> seq;
    set<set<string>> ret;
    dfs(0, n, seq, ret);

    return ret.size()
}

// [solve] 첫번째 시도: 가능한 아이디로 수열을 만들었지만, 수열 중복 체크하기가 쉽지 않았음. 
//  
// 1. banned_id를 순회하며 가능한 id를 set 배열에 담는다.
// 2. set 각 배열에서 원소를 하나씩 골라 가능한 경우를 vector에 담는다. vector에 하나씩 옮겨 담을 때 현재 담은 원소를 제외한 원소를 담을 수 없다면 건너뛴다.
// 3. vector 배열에 있는 원소를 순회하며, 하나라도 ret(set)에 없다면 담는다. (개수를 센다)
// 
// unordered_set<string> s[8];
// unordered_set<string> ret;
// 
// bool is_banned_id(string ban, string user) {
//     int idx = 0;
//     
//     if (ban.length() != user.length())
//         return false;
//     
//     while (ban[idx]) {
//         if (ban[idx] == '*') {
//             ++idx;
//             continue;
//         }
//         if (ban[idx] == user[idx])
//             ++idx;
//         else {
//             return false;
//         }
//     }
//     return true;
// }
// 
// int solution(vector<string> user_id, vector<string> banned_id) {
//     
//     for (int i = 0; i < banned_id.size(); ++i) {
//         string banned = banned_id[i];
//         for (int j = 0; j < user_id.size(); ++j) {
//             if (is_banned_id(banned, user_id[j])) {
//                 s[i].insert(user_id[j]);
//             }
//         }
//     }
//     int n = banned_id.size();
//     for (int i = 0; i < n; ++i) {
//         for (auto e : s[i])
//             cout << "e: " << e << ' ';
//         cout << '\n';
//     }
//     int answer = 0;
//     return answer;
// }

#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>

using namespace std;

void recur(string name, int income, unordered_map<string, int>& profits, unordered_map<string, string>& parent) {
    if (name == "-" || income < 1)
        return;
    int fee = income * 0.1;
    profits[name] += income - fee;
    recur(parent[name], fee, profits, parent);
}

vector<int> solution(vector<string> enroll, vector<string> referral, vector<string> seller, vector<int> amount) {
    
    unordered_map<string, string> parent;
    unordered_map<string, int> profits;
    
    for (auto& e : enroll) {
        profits[e] = 0;
    }
    for (int i = 0; i < enroll.size(); ++i) {
        parent[enroll[i]] = referral[i];
    }

    for (int i = 0; i < seller.size(); ++i) {
        int total_profit = 100 * amount[i];
        recur(seller[i], 100 * amount[i], profits, parent);
    }
    
    vector<int> ans;
    for (auto& e : enroll) {
        ans.push_back(profits[e]);
    }
    return ans;
}


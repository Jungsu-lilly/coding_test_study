#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<long long> nums;

bool is_prime(long long num) {

    if (num <= 1)
        return false;
    
    if (num == 2) 
        return true;
    
    for (int i = 3; i <= num / i; ++i) {
        if (num % i == 0) return false;
    }
    
    return true;
}

void find_nums(string& converted) {
    
    string num = "0";
    for (int i = 0; i < converted.length(); ++i) {
        if (converted[i] == '0') {
            nums.push_back(stol(num));
            num = "0";
            continue;
        }
        num += converted[i];
    }
    nums.push_back(stol(num));
}

string convert_base(int n, int k) {
    
    string base = "0123456789";
    
    if (n == 0)
        return "0";
    
    string ans = "";
    while (n > 0) {
        ans.push_back(base[n % k]);
        n /= k;
    }
    
    reverse(ans.begin(), ans.end());
    return ans;
}

int solution(int n, int k) {
    
    string converted = convert_base(n, k);
    
    find_nums(converted);
    
    int ans = 0;
    for (auto e : nums) {
        if (is_prime(e)) {
            ++ans;
        }
    }
    return ans;
}

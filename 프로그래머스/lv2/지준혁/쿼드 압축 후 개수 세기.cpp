#include <string>
#include <vector>
#include <iostream>

using namespace std;

bool is_compress(int n, int r, int c, vector<vector<int>>& arr, int& zero, int& one) {
    int st = arr[r][c];
    for (int i = r; i < n + r; ++i) {
        for (int j = c; j < n + c; ++j) {
            if (arr[i][j] != st) return false;
        }
    }
    st == 0 ? zero++ : one++;
    return true;
}

void recur(int n, int r, int c, vector<vector<int>>& arr, int& zero, int& one) {
    
    if (n == 0 || is_compress(n, r, c, arr, zero, one)) {
        
        return; 
    }
    int half = n / 2;
    recur(half, r, c, arr, zero, one);
    recur(half, r, c + half, arr, zero, one);
    recur(half, r + half, c, arr, zero, one); 
    recur(half, r + half, c + half, arr, zero, one);
}
    
vector<int> solution(vector<vector<int>> arr) {
    vector<int> ans = {0 , 0};
    recur(arr.size(), 0, 0, arr, ans[0], ans[1]);
    return ans;
}

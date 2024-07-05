#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

// 이진 탐색을 이용.
// 돌다리 최댓값이 건널 수 있는 사람의 최댓값을 의미.
bool cross_stones(vector<int>& stones, int k, int people) {
    int step = 0;
    for (auto& e : stones) {
        if (e < people) {
            ++step;
            if (step >= k) {
                return false;
            }
        } else {
            step = 0;
        }
    }
    return true;
}

int solution(vector<int> stones, int k) {

    int ans = 0;
    int st = 0;
    int en = *max_element(stones.begin(), stones.end());
    while (st <= en) {
        int people = (st + en) / 2;
        if (cross_stones(stones, k, people)) {
            st = people + 1;
            ans = max(ans, people);
        } else {
            en = people - 1;
        }
    }

    return ans;
}

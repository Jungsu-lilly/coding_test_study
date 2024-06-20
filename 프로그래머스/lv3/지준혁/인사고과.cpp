#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

// 1. 이중 반복문 풀이는 시간초과 (n = 100'000)
// 2. 총점으로 정렬, (순서 기억))
//    총점이 높거나 같은데 인센티브를 받을 수 없는 경우는 없다.
//    {4, 0} {5, 1}, {5, 2}, {5, 3}, {3, 4}
//    -> 정렬 {5, 1}, {5, 2}, {5, 3}, {4, 0}, {3, 4}
//    이 경우 순위는 알 수 있는데, 완호가 인센티브 제외 여부를 알 수는 없다. 어떻게 알 수 있을까?
//    가장 총점이 높은 사람만 비교해도 되지 않을까? 안됨
//    1등: {1, 7} => 8, 2등: {3, 3} => 6, 완호 {2, 0}
//    완호보다 순위가 높은 사람들 모두랑 비교해도 되지 않을까? -> 가능해보임
//	  -> 완호가 공등 1등인 경우 처리를 못함.

vector<pair<int, int>> sco;

int solution(vector<vector<int>> scores) {
    
    for (int i = 0; i < scores.size(); ++i) {
        int sum = 0;
        for (auto e : scores[i]) {
            sum += e;
        }
        sco.push_back({sum, i});
    }
    
  	sort(sco.begin(), sco.end(), [](auto& a, auto& b) {
        return a > b;
    });    
    
    int rank = 2;
    int wanho_rank = 1;
    for (int i = 0; i < sco.size(); ++i) {
        cout << sco[i].first << ' ' << sco[i].second << '\n';
        if (sco[0].second == 0) break;
        if (i == 0) continue;
        if (sco[i].first < sco[i - 1].first) // 이전사람이 점수가 더 높다면 등수 올림
            ++rank;
        if (sco[i].second == 0) {
            wanho_rank = rank;
        }
    }
    
    bool is_not_incentive = false;
    for (int i = 0; i < rank; ++i) {
        int index = sco[i].second;
        if (scores[0][0] < scores[index][0] && scores[0][1] < scores[index][1]) {
            is_not_incentive = true;
        }
    }
    if (is_not_incentive) {
        return -1;
    }
    return rank;
}

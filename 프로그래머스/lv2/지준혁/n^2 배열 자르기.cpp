#include <string>
#include <vector>
#include <algorithm>

using namespace std;

// 1 2 3
// 2 2 3
// 3 3 3
// -> 1 2 {3 2 2 3} 3 3 3
// 규칙을 찾을 수 있니?
// n = 3, 시작인덱스: 1
// 0 -> (0, 0)
// 1 -> (0, 1)
// 2 -> (0, 2)
// 3 -> (1, 0)
// 4 -> (1, 1)
// 5 -> (1, 2)
// 6 -> {2, 0}, {2, 1}, {2, 2}
//
// 규칙에 따라 숫자를 채워넣는 방식 최소 100만^2 시간초과
// 인덱스를 뽑아서 규칙 찾아내는 방식
vector<int> solution(int n, long long left, long long right) {
    
    vector<int> answer;
    for (long long i = left; i <= right; ++i) {
        long long share = i / n;
        long long remainder = i % n;
        answer.push_back(max(share, remainder) + 1);
    }
    return answer;
}

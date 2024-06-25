#include <string>
#include <vector>

using namespace std;

bool solution(vector<vector<int>> key, vector<vector<int>> lock) {
    bool answer = true;
    
    check_unlock(); // key에 있는 값을 lock으로 옮겼을 떄 lock이 다 1로 되는지
    
    int len = 
    for (int roate = 0; rotate < 4; ++rotate) {
        rotate_key(); // 키 90도 회전 시키기
                      // key 상하좌우로 이동 가능한 경우의 수 4^20? 시간초과//
    }
    
    return answer;
}

#include <string>
#include <vector>

using namespace std;

// 1. 자물쇠 영역을 키의 길이 비례해서 늘린다.
// 2. 자물쇠 (0, 0)부터 늘어진 자물쇠 길이에서 열쇠의 길이만큼 차감한 부분(n - k + 1, n - k + 1)까지 열쇠를 맞춰본다. 이때, 열쇠의 돌기 부분과 자물쇠의 홈 부분이 정확히 일치해야 한다.
// 3. 2번 과정에서 맞는 열쇠가 없다면 열쇠를 90도 회전한다.
// 4. 맞는 열쇠가 없다면 false, 있다면 true를 반환한다.
int locks[64][64] = {};
int hole;

void rotate_key(vector<vector<int>>& key) {
    int tmp[24][24] = {};
    int k = key.size();
    
    for (int i = 0; i < k; ++i) {
        for (int j = 0; j < k; ++j) {
            tmp[j][k - i - 1] = key[i][j];
        }
    }
    for (int i = 0; i < k; ++i) {
        for (int j = 0; j < k; ++j) {
            key[i][j] = tmp[i][j];
        }
    }
}

bool is_unlock(int y, int x, vector<vector<int>>& key, int hole) {
    
    int k = key.size();
    for (int i = y; i < y + k; ++i) {
        for (int j = x; j < x + k; ++j) {
            if (locks[i][j] == 2 && key[i - y][j - x] == 1) {
                return false;
            }
            if (locks[i][j] == 1 && key[i - y][j - x] == 1) {
                --hole;
            }
        }
    }
    return hole == 0;
}


bool solution(vector<vector<int>> key, vector<vector<int>> lock) {
    
    int k = key.size();
    int l = lock.size();
    for (int i = 0; i < l; ++i) {
        for (int j = 0; j < l; ++j) {
            if (lock[i][j] == 0) {
                ++hole;
            }
            locks[i + k - 1][j + k - 1] = lock[i][j] + 1;  
        }
    }
    int n = 2 * (k - 1) + l;
    
    for (int rot = 0; rot < 4; ++rot) {
        rotate_key(key);
        for (int i = 0; i < n - k + 1; ++i) {
            for (int j = 0; j < n - k + 1; ++j) {
                if (is_unlock(i, j, key, hole)) return true;
            }
        }
    }
    return false;
}

// bool solution(vector<vector<int>> key, vector<vector<int>> lock) {
//     bool answer = true;
//     
//     check_unlock(); // key에 있는 값을 lock으로 옮겼을 떄 lock이 다 1로 되는지
//     
//     int len = 
//     for (int roate = 0; rotate < 4; ++rotate) {
//         rotate_key(); // 키 90도 회전 시키기
//                       // key 상하좌우로 이동 가능한 경우의 수 4^20? 시간초과//
//     }
//     
//     return answer;
// }

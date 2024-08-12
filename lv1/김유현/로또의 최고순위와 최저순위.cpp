#include <string>
#include <vector>
#include <algorithm>

using namespace std;

// 정답 개수 - 랭크 
int ranks[7] = {6, 6, 5, 4, 3, 2, 1};

// 정답 여부
bool winNum[46];

vector<int> solution(vector<int> lottos, vector<int> win_nums) {
    vector<int> answer;
    
    for(int num : win_nums) {
        winNum[num] = true;
    }
    
    int zeroCnt = 0;
    int winCnt = 0;
    
    for(int lotto : lottos) {
        if (lotto == 0) {
            zeroCnt++;
        } else if (winNum[lotto]) {
            winCnt++; 
        }
    }
    
    int maxRank = ranks[zeroCnt + winCnt];
    int minRank = ranks[winCnt];
   
    answer.push_back(maxRank);
    answer.push_back(minRank);
    
    return answer;
}
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> lottos, vector<int> win_nums) {
    vector<int> answer;
    int match = 0, zeros = 0;
    for(int i=0; i<lottos.size(); i++) {
        if(lottos[i] == 0) zeros++;
        else {
            auto it = find(win_nums.begin(), win_nums.end(), lottos[i]);
            if(it != win_nums.end()) match++;
        }
    }

    int min_rank = 7 - match;
    int max_rank = 7 - (match + zeros);

    if(min_rank > 6) min_rank = 6;
    if(max_rank > 6) max_rank = 6;


    answer.push_back(max_rank);
    answer.push_back(min_rank);

    return answer;
}
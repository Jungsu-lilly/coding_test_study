#include <string>
#include <vector>
#include <tuple>

using namespace std;

// 미해결.. 오늘중으로 다시 올리겠습니다..!

vector<string> solution(vector<vector<int>> line) {
    vector<string> answer;
    vector<pair<int,int>> spots;
    for(int i=0; i<line.size(); i++) {
        for(int j=i+1; j<line.size(); j++) {
            double a1, a2, b1, b2, c1, c2;
            tie(a1, b1, c1) = line[i];
            tie(a2, b2, c2) = line[j];
            
            double determinant = a1 * b2 - a2 * b1;
            if(determinant == 0) continue;
            else {
                double x = (b1*c2 - b2*c1) / determinant;
                double y = (a2*c1 - a1*c2) / determinant;
                if(floor(x)==x && floor(y)==y)
                    spots.push_back(make_pair(x,y));
            }
        }
    }
    
    return answer;
}
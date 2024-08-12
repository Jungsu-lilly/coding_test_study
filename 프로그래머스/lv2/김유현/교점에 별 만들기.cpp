#include <string>
#include <vector>
#include <iostream>
#include <set>
#define INF 987654321

using namespace std;

bool isDivisible(int xNumerator, int yNumerator, int denominator) {
    return xNumerator % denominator == 0 && yNumerator % denominator == 0;
}

vector<string> solution(vector<vector<int>> line) {
    vector<string> answer;
    set<pair<int, int>> meets; 
    
    for(int i=0; i<line.size()-1; i++) {
        for(int j=i+1; j<line.size(); j++) {
            int a = line[i][0], b = line[i][1], e = line[i][2];
            int c = line[j][0], d = line[j][1], f = line[j][2];
            
            int denominator = a*d - b*c;

            if (denominator == 0) {
                continue;
            } else {
                int xNumerator = b*f - e*d;                
                int yNumerator = e*c - a*f;
                
                
                if (isDivisible(xNumerator, yNumerator, denominator)) {
                    int x = xNumerator / denominator;
                    int y = yNumerator / denominator;
                    
                    meets.insert({x, y});
                }
            }
        }
    }
    
    int minX = INF;
    int maxX = -INF;
    int minY = INF;
    int maxY = -INF;
    
    for(auto i : meets) {
        cout << i.first << "," << i.second << "\n";
        
        minX = min(i.first, minX);
        maxX = max(i.first, maxX);
        
        minY = min(i.second, minY);
        maxY = max(i.second, maxY);
    }
    
    cout << minX << "~" << maxX << "\n";
    cout << minY << "~" << maxY << "\n";

    return answer;
}
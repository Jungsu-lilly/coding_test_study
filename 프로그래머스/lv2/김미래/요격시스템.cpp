#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

int solution(vector<vector<int>> targets) {
    int answer = 0;
    int index = 0; 
    sort(targets.begin(), targets.end());
    
    while(index<targets.size()){
        int mark = targets[index][1];
        answer++;
        
        while(index<targets.size() && mark>targets[index][0]){
            if(mark>targets[index][1]){
                mark = targets[index][1];
            }
            index++;
        }
      
    }
    return answer;
}

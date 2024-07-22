#include <string>
#include <vector>
#include <iostream>
using namespace std;

vector<vector<int>> solution(vector<vector<int>> arr1, vector<vector<int>> arr2) {
    vector<vector<int>> answer;
    for(int i=0; i<arr1.size(); i++){
        vector<int> v;
          for(int k=0; k<arr2[0].size(); k++){
                      int result = 0;
                for(int m=0; m<arr2.size(); m++){
           
                    result += arr1[i][m] * arr2[m][k];
                  
                }
          v.push_back(result);
        }
        answer.push_back(v);
    }
    return answer;
}

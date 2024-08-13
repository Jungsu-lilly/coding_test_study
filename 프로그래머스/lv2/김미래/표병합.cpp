#include <string>
#include <vector>
#include <algorithm>
using namespace std;
int column;

bool compare(vector<int> data1, vector<int> data2){
    if(data1[column-1] == data2[column-1]){
        return data1[0] > data2[0];
    }else{
        return data1[column-1]<data2[column-1];
    }
}
int solution(vector<vector<int>> data, int col, int row_begin, int row_end) {
    int answer = 0;
    column = col;
    sort(data.begin(), data.end(), compare);
    
    for(int j=row_begin-1; j<=row_end-1; j++){
        int result = 0;
        
      for(int i=0; i<data[0].size(); i++){
         result += data[j][i] % (j+1);
      }
            answer ^= result;
    }
 
    
    return answer;
}

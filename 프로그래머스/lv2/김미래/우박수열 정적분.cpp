#include <string>
#include <vector>
#include <iostream>
using namespace std;

vector<double> solution(int k, vector<vector<int>> ranges) {
    vector<double> answer;
    vector<double> width;
    
    while(k!=1){
        int nextK=0;
        if(k %2 == 0){
            nextK = k/2;
        }else{
            nextK= (k*3) +1;
        }
        width.push_back((k + nextK) / 2.0);
        k = nextK;
    }
    
    for(int i=0; i<ranges.size(); i++){
        int start = ranges[i][0];
        int end = ranges[i][1]+width.size();
        double curWidth = 0;
       
        if(end<start){
            answer.push_back(-1.0);
        }
        else{
            for(int j=start; j<end; j++){
             
                curWidth+=width[j];
            }
            answer.push_back(curWidth);
        }
    }
    
    return answer;
}

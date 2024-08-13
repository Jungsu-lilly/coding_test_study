#include <string>
#include <vector>
#include <algorithm>
#include <string>
#include <iostream>
using namespace std;
bool compare(string num1, string num2){

    return num1+num2>num2+num1;
}

string solution(vector<int> numbers) {
    string answer = "";
    vector<string> strNum;
  
    for(int i=0; i<numbers.size(); i++){
        strNum.push_back(to_string(numbers[i]));
    }
    
    sort(strNum.begin(), strNum.end(), compare);
    
    for(int i=0; i<strNum.size(); i++){
        answer += strNum[i];
    }
    
    if(strNum[0]=="0"){
       answer = "0";
    }
    
    return answer;
}

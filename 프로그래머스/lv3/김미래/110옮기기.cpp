#include <string>
#include <vector>
#include <iostream>
using namespace std;
string manipulate(string str){
    int count = 0;
    string temp = "";

    for(int j = 0; j < str.length(); j++){
        temp += str[j];
        if(temp.length() >= 3){
            if(temp.substr(temp.length() - 3) == "110"){
                temp.erase(temp.length() - 3, 3);
                count++;
            }
        }
    }
    str = temp;

    int index = -1;
    for(int j = str.length() - 1; j >= 0; j--){
        if(str[j] == '0') {
            index = j;
            break;
        }
    }

    string result="";
    if(index == -1){
        for(int k=0; k<count; k++){
            result += "110";
        }
        result += str;
    } else {
        for(int j = 0; j < str.length(); j++){
            if(j == index){
                result += str[j];
                for(int k=0; k<count; k++){
                    result +="110";
                }
            }else{
                result+=str[j];
            }
        }
    }
    return result;
}
vector<string> solution(vector<string> s) {
    vector<string> answer;

    for(int i=0; i<s.size(); i++){
        string finishedOne = manipulate(s[i]);
        answer.push_back(finishedOne);
    }
     

    return answer;
}

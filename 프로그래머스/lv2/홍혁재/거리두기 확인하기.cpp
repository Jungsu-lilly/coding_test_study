#include <string>
#include <vector>
#include <cmath>

using namespace std;

int check(vector<string> place, int st_row, int st_col) {
   for(int i = st_row; i < 5; i++) {
       if(abs(st_row - i) > 2) break;
       
       for(int j = 0; j < 5; j++) {
           if(i == st_row && j == st_col)  continue;
           if(abs(st_row - i) + abs(st_col - j) > 2) continue;
           if(place[i][j] != 'P') continue;
           if(st_row - i == 0) {
               if(abs(st_col - j) == 1) return 0;
                   if(place[i][(st_col + j) / 2] == 'X')
                       continue;
                   else 
                       return 0;
           }
               if(st_col - j == 0) {
                   if(abs(st_row - i) == 1) return 0;
                   if(place[(st_row + i) / 2][j] == 'X')
                       continue;
                   else
                       return 0;
               } 
           if(place[st_row][j] != 'X' || place[i][st_col] != 'X') return 0;
       }
   } 
    return 1;
}

vector<int> solution(vector<vector<string>> places) {
    vector<int> answer;
    int flag;
    
   	for(vector<string> place : places) {
        flag = 1;
       for(int i = 0; i < 5; i++) {
           for(int j = 0; j < 5; j++) {
               if(place[i][j] != 'P') continue;
               else {
                   if(check(place, i, j) == 0) {
                       flag = 0;
                       break;
                   }
               }
           }
           if(flag == 0) break;
       } 
        answer.push_back(flag);
    } 
    return answer;
}
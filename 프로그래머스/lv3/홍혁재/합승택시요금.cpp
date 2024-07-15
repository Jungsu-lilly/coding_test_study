/*
알고리즘: 다익스트라
*/
#include <string>
#include <vector>

using namespace std;

int** a;
int inf = 99999999;

int solution(int n, int s, int a, int b, vector<vector<int>> fares) {
    int answer = 0;
    
    a = new int*[n];
    for(int i = 0; i < n; i++) {
        a[i] = new int[n] {inf};
    }
    
    for(auto fare : fares) {
        a[fare[0]][fare[1]] = fare[2];
        a[fare[1]][fare[1]] = fare[2];
    }
    
    return answer;
}
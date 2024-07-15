/*
알고리즘: 브루트 포스
*/

#include <string>
#include <vector>

using namespace std;

int bf(vector<int> numbers, int target, int x, int total) {
    if(x >= numbers.size()) {
        if(total == target) return 1;
        else return 0;
    }
    for(int i = x; i < numbers.size(); i++) {
        return bf(numbers, target, i + 1, total + numbers[i]) + 
            bf(numbers, target, i + 1, total - numbers[i]);;
    }
}

int solution(vector<int> numbers, int target) {
    int answer = 0;
    
    answer = bf(numbers, target, 0, 0);
    
    return answer;
}
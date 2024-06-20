#include <string>
#include <vector>
#include <stack>
#include <iostream>

using namespace std;

// stack을 활용
// 1. 뒤에서 부터 numbers 원소를 확인하면서 스택에 담는다.
// 2. 스택이 비어있지 않을 때
//    1) 스택의 원소가 추가될 원소보다 크다면 스택의 원소를 뒷 큰수에 추가
//    2) 스택의 원소가 추가될 원소보다 작거나 같다면 스택을 뒷 큰수가 나올 떄까지 탐색, 없다면 -1 
// 3. 스택이 비어있다면
//    뒷 큰수가 없으므로 -1

vector<int> solution(vector<int> numbers) {
    
    stack<int> s;
    stack<int> ans;

    for (int i = numbers.size() - 1; i >= 0; --i) {
        if (!s.empty()) {
            if (s.top() > numbers[i]) {
                ans.push(s.top());
            }
            else {
                while (!s.empty()) {
                    if (s.top() > numbers[i]) {
                        ans.push(s.top());
                        break;
                    }
					B
                    s.pop();                    
                }
                if (s.empty()) {
                    ans.push(-1);
                }
            }
        } else {
            ans.push(-1);
        }
        s.push(numbers[i]);
    }
   
    vector<int> answer;
    while (!ans.empty()) {
        answer.push_back(ans.top());
        ans.pop();
    }
    return answer;
}

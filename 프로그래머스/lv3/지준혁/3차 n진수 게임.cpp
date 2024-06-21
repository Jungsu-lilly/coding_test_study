#include <string>
#include <vector>
#include <iostream>
#include <stack>
#include <queue>

using namespace std;

// 1. 진법 수를 0~1000까지 구함.
// 2. 구한 진법 수를 순서에 맞게 정답 배열에 담음
// 테케 10개 못맞춘 코드

vector<char> nums;

void convert_base(int num, int base) {
    
    if (num == 0) {
        nums.push_back('0');
        return;
    }
    stack<char> s;
    while (num > 0) {
        int number = num % base;
        s.push('0' + (num % base));
        num /= base;
    }
    while (!s.empty()) {
        nums.push_back(s.top());
        s.pop();
    }
}

void convert_base11(int num, int base, string base11) {
    
    if (num == 0) {
        nums.push_back('0');
        return;
    }
    stack<char> s;
    while (num > 0) {
        int number = num % base;
        s.push(base11[number]);
        num /= base;
    }
    while (!s.empty()) {
        nums.push_back(s.top());
        s.pop();
    }
}

void convert_base12(int num, int base, string base12) {
    
    if (num == 0) {
        nums.push_back('0');
        return;
    }
    stack<char> s;
    while (num > 0) {
        int number = num % base;
        s.push(base12[number]);
        num /= base;
    }
    while (!s.empty()) {
        nums.push_back(s.top());
        s.pop();
    }
}

void convert_base13(int num, int base, string base13) {
    
    if (num == 0) {
        nums.push_back('0');
        return;
    }
    stack<char> s;
    while (num > 0) {
        int number = num % base;
        s.push(base13[number]);
        num /= base;
    }
    while (!s.empty()) {
        nums.push_back(s.top());
        s.pop();
    }
}

void convert_base14(int num, int base, string base14) {
    
    if (num == 0) {
        nums.push_back('0');
        return;
    }
    stack<char> s;
    while (num > 0) {
        int number = num % base;
        s.push(base14[number]);
        num /= base;
    }
    while (!s.empty()) {
        nums.push_back(s.top());
        s.pop();
    }
}

void convert_base15(int num, int base, string base15) {
    
    if (num == 0) {
        nums.push_back('0');
        return;
    }
    stack<char> s;
    while (num > 0) {
        int number = num % base;
        s.push(base15[number]);
        num /= base;
    }
    while (!s.empty()) {
        nums.push_back(s.top());
        s.pop();
    }
}

void convert_base16(int num, int base, string base16) {
    
    if (num == 0) {
        nums.push_back('0');
        return;
    }
    stack<char> s;
    while (num > 0) {
        int number = num % base;
        s.push(base16[number]);
        num /= base;
    }
    while (!s.empty()) {
        nums.push_back(s.top());
        s.pop();
    }
}

string solution(int n, int t, int m, int p) {
    
    string base11 = "0123456789A";
    string base12 = "0123456789AB";
    string base13 = "0123456789ABC";
    string base14 = "0123456789ABCD";
    string base15 = "0123456789ABCDE";
    string base16 = "0123456789ABCDEF";    
    
    int st = 0;
    while (st <= 1000) {
        if (n <= 10) {
            convert_base(st, n);
        } else if (n == 11) {
            convert_base11(st, n, base11);
        } else if (n == 12) {
            convert_base12(st, n, base12);

        } else if (n == 13) {
            convert_base13(st, n, base13);

        } else if (n == 14) {
            convert_base14(st, n, base14);

        } else if (n == 15) {
            convert_base15(st, n, base15);

        } else if (n == 16) {
            convert_base16(st, n, base16);

        }
        // cout << "nums: ";
        // for (auto e : nums) {
        //     cout << e << ' ';
        // }
        // cout << '\n';
        ++st;
    }
    
    string answer = "";
    int turn = 1;
    int cnt = 0;    
    int tube = p;
    for (auto e : nums) {
        if (turn == tube) {
            answer.push_back(e);
            tube += m;
            ++cnt;
            if (cnt == t)
                break;
        } 
        turn++;
    }
    return answer;
}

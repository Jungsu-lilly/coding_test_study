#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(vector<int> arrayA, vector<int> arrayB) {
    
    sort(arrayA.begin(), arrayA.end());
    sort(arrayB.begin(), arrayB.end());
    vector<int> numsA;
    vector<int> numsB;
    for (int i = 2; i <= arrayA[0]; ++i) {
        if (arrayA[0] % i == 0) {
            numsA.push_back(i);
        }
    }
    for (int i = 2; i <= arrayB[0]; ++i) {
        if (arrayB[0] % i == 0) {
            numsB.push_back(i);
        }
    }
    
    for (int i = 1; i < arrayA.size(); ++i) {
        for (int j = numsA.size() - 1; j >= 0; --j) {
            if (arrayA[i] % numsA[j] != 0) {
                numsA.erase(numsA.begin() + j);
            }
        }
    }
    for (int i = 1; i < arrayB.size(); ++i) {
        for (int j = numsB.size() - 1; j >= 0; --j) {
            if (arrayB[i] % numsB[j] != 0) {
                numsB.erase(numsB.begin() + j);
            }
        }
    }
    
    pair<int, int> ret = {0, 0};
    for (int j = numsA.size() - 1; j >= 0; --j) {
        bool is_devide = false;
        for (int i = 0; i < arrayB.size(); ++i) {
            if (arrayB[i] % numsA[j] == 0) {
                is_devide = true;
            }
        }
        if (!is_devide) {
            ret.first = numsA[j];
            break;
        }
    }
    for (int j = numsB.size() - 1; j >= 0; --j) {
        bool is_devide = false;
        for (int i = 0; i < arrayA.size(); ++i) {
            if (arrayA[i] % numsB[j] == 0) {
                is_devide = true;
            }
        }
        if (!is_devide) {
            ret.second = numsB[j];
            break;
        }
    }
    return max(ret.first, ret.second);
}



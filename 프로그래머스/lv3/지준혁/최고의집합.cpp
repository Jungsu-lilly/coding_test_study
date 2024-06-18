#include <string>
#include <vector>
#include <iostream>

using namespace std;

// 자연수 n개로 이루어진 중복 집합!!
// 자연수 2개로 이루어진 집합 중 합이 9가 되는 집합 -> {1, 8}, {2, 7}, {3, 6}, {4, 5} 
// 자연수 3개로 이루어진 집합 중 합이 9가 되는 집합 -> {1, 1, 1}, {1, 1, 7}, {1, 2, 6}, {1, 3, 5} ...
// 자연수 4개로 이루어진 집합 중 합이 9가 되는 집합 -> {1, 1, 1, 6} 

// [Solve]
// 값이 균등할수록 곱셈의 결과가 커짐
// 쉬운 예로 가로 세로의 길이가 합쳐서 8일 때 넓이를 가장 크게 구하려면?
// 4 * 4 = 16
// 5 * 3 = 15
// 6 * 2 = 12
// 7 * 1 = 7

vector<int> solution(int n, int s) {

    int share = s / n;
    int remainder = s % n;

    if (share < 1) return {-1};

    vector<int> answer(n, share);
    for (int i = 0; i < remainder; ++i) {
        answer[n - i - 1] += 1;
    }
    return answer;
}

// [Solve] 처음 시도한 풀이 
// 1. 각 원소의 합이 S가 되면서, 원소의 곱이 최대가 되어야 한다.
// 2. 먼저 가능한 원소 수를 구해야함. n개 뽑아야 함. -> DFS
// 3. N개의 원소를 합해서 합이 S가 나오는 순열 구함.
// 4. 최대값을 갱신할 때 순열도 갱신해서 <answer>로 반환함.
// O(9^N) 당연히 시간초과

int is_selected[10'004];
int multiple_sum = 0;
vector<int> answer; 

void dfs(int depth, int sum, int n, int s) {
    
    if (depth == n) {
		if (sum == s) {
			int cur_multiple_sum = 1;
			for (int i = 0; i < n; ++i) {
				cur_multiple_sum *= is_selected[i];
			}		
			if (cur_multiple_sum > multiple_sum) {
				multiple_sum = cur_multiple_sum;
				answer = vector<int>(is_selected, is_selected + n);
			}
		}
		return;
    }

	for (int i = 1; i <= 9; ++i) {
		is_selected[depth] = i;
		dfs(depth + 1, sum + i, n, s);
	}
}

vector<int> solution(int n, int s) {
    
    dfs(0, 0, n, s);

    return answer;
}



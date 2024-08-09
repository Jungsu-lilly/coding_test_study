#include <string>
#include <vector>
#include <iostream>
#include <cmath>

using namespace std;

vector<int> positions;

vector<double> solution(int k, vector<vector<int>> ranges) {
    vector<double> answer;

    int curY = k;
    positions.push_back(curY);

    while (curY != 1)
    {
        if (curY % 2 == 0) curY /= 2;
        else curY = curY * 3 + 1;

        positions.push_back(curY);
    }

    for (int cnt = 0; cnt < ranges.size(); ++cnt)
    {
        double res = 0;

        int a = ranges[cnt][0];
        int b = ranges[cnt][1];

        if (b == 0) b = positions.size() - 1;
        else if (b < 0) b = positions.size() - 1 + b;

        if (a > b) answer.push_back(-1.0);
        else
        {
            int aX = a;
            int bX = a + 1;
            while (bX <= b)
            {
                res += ((double)(positions[aX] + positions[bX])) / 2;
                aX++;
                bX++;
            }

            answer.push_back(res);
        }

        // 0, 1 이었다면 0의 높이와 1의 높이를 더한 값 * 2 /2
    }

    return answer;
}
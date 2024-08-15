#include <string>
#include <vector>
#include <map>

using namespace std;

map<int, int> m;

int solution(vector<int> a) {
    int answer = 0;

    for (int cnt = 2; cnt < a.size(); ++cnt) m.insert({ a[cnt], a[cnt] });

    int frontMin = a[0];
    int rearMin = (*m.begin()).first;

    answer++;

    for (int cnt = 1; cnt < a.size(); ++cnt)
    {
        int reserveNum = a[cnt];
        int minCnt = 0;

        if (reserveNum > frontMin) ++minCnt;

        rearMin = (*m.begin()).first;

        if (reserveNum > rearMin) ++minCnt;

        if (minCnt < 2) ++answer;

        m.erase(reserveNum);
        frontMin = min(frontMin, reserveNum);
    }

    return answer;
}
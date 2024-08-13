#include <string>
#include <vector>

using namespace std;

int solution(string s)
{
    int answer = 0, countDifferent = 0, countSame = 1;
    char x = s[0];
    for (int i = 1; i < s.size(); i++)
    {
        if (s[i] == x)
            countSame++;
        else
            countDifferent++;
        if (countDifferent == countSame)
        {
            answer++;
            x = s[i + 1];
            countDifferent = 0;
            countSame = 0;
        }
    }
    // 남은 문자열 처리
    if (countSame != countDifferent)
        answer++;
    return answer;
}
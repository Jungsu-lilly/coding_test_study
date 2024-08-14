#include <string>
#include <vector>

using namespace std;

string solution(string s, string skip, int index)
{
    string answer = "";
    for (auto i : s)
    {
        int count = 0;
        while (count < index)
        {
            i++;
            if (i > 'z')
                i = 'a';
            if (skip.find(i) == string::npos)
                count++;
        }
        answer += i;
    }
    return answer;
}
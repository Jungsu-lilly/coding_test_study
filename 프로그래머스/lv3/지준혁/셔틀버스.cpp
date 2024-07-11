#include <string>
#include <vector>
#include <sstream>
#include <iostream>

using namespace std;


// [solve] 풀이
// #include <string>

int convert_minutes(string& arrive_time) {
    int hours, minutes;
    char colon;
    istringstream iss(arrive_time);
    iss >> hours >> colon >> minutes;

    return hours * 60 + minutes;
}

string convert_string(int mins) {
    int hours = mins / 60;
    int minutes = mins % 60;
    ostringstream oss;
    oss << (hours < 10 ? "0" : "") << hours << ":" << (minutes < 10 ? "0" : "") << minutes;

    return oss.str();
}

string solution(int n, int t, int m, vector<string> timetable) {

    string answer = "";
    queue<int> bus;
    queue<int> crew;

    sort(timetable.begin(), timetable.end());

    for (auto e : timetable) {
        crew.push(convert_minutes(e));
    }

    for (int i = 0; i < n; ++i) {
        bus.push(9 * 60 + t * i);
    }

    while (bus.size() > 1) {
        int bus_arrive = bus.front();
        bus.pop();
        for (int i = 0; i < m; ++i) {
            if (!crew.empty() && crew.front() <= bus_arrive) {
                crew.pop();
            }
        }
    }

    if (crew.size() >= m) {
        int crew_last_time = 0;
        for (int i = 0; i < m; ++i) {
            crew_last_time = crew.front();
            crew.pop();
        }
        answer = convert_string(min(crew_last_time - 1, bus.front()));
    } else {
        answer = convert_string(bus.front());
    }

    return answer;
}

// [solve] 첫 번째 시도 
// 5시에 버스가 오고, 2시에 버스가 옴 (정원 각 2명)
// 2시에 4명이 기다리고 있음.
// 버스에 타려면 1시 59분에는 도착해야 함.
// 1. 마지막 버스 도착 시간을 계산한다.
// 2. 마지막 버스를 타기 위해서 마지막 버스에 타는 사람들의 시간을 계산하고(앞에서 버스부터 버스에 태움), 정원에 여유가 있다면 버스 도착 시간, 여유가 없다면 마지막 도착한 사람보다 1분 더 빨리. (정각이면 시간내림 계산)

// vector<string> split(string& str) {
//     vector<string> tokens;
//     string token;
//     istringstream tokenStream(str);
//     while (getline(tokenStream, token, ':')) {
//         tokens.push_back(token);
//     }
//     return tokens;
// }
// 
// string solution(int n, int t, int m, vector<string> timetable) {
//     cout << timetable.size() << '\n';
//     pair<int, int> arrive_time[timetable.size()];
//     
//     int idx = 0;
//     for (auto e : timetable) {
//         vector<string> tokens = split(e);
//         arrive_time[idx].first = stoi(tokens[0]);
//         arrive_time[idx].second = stoi(tokens[1]);
//         cout << arrive_time[idx].first << ' ' << arrive_time[idx].second << '\n';
//         ++idx;
//     }
//     
//     string answer = "";
//     return answer;
// }

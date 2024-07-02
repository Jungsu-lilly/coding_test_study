#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <unordered_map>
#include <iostream>

using namespace std;

vector<tuple<string, string, int>> music;

bool is_match(string& a, string& b) {
    if (a.length() < b.length()) return false;

    for (int i = 0; i < a.length() - b.length() + 1; ++i) {
        int idx = i;
        bool is_matched = true;
        for (int j = 0; j < b.length(); ++j) {
            if (a[idx + j] != b[j]) {
                is_matched = false;
                break;
            }
            if (j == b.length() - 1 && idx + j + 1 < a.length()) {
                if (a[idx + j + 1] == '#') is_matched = false;
            }
        }

        if (is_matched) return true;
    }
    return false;
}

void make_music(string& m) {
    
    istringstream iss(m);
    vector<string> split;
    string tmp;
    while (getline(iss, tmp, ',')) {
        split.push_back(tmp);
    }
    int st = stoi(split[0]) * 60 + stoi(split[0].substr(3));
    int end = stoi(split[1]) * 60 + stoi(split[1].substr(3));
    int playing = end - st;    

    int idx = 0;
    string gasa = "";
    int time = playing;
    while (time) {
        char append = split[3][(idx % split[3].length())];
        gasa += append;
        ++idx;
        if (append == '#') continue;
        --time;
    }
    if (split[3][(idx % split[3].length())] == '#') {
        gasa += '#';
    }
    music.push_back({split[2], gasa, playing});
}

string solution(string m, vector<string> musicinfos) {
    
   
    for (int i = 0; i < musicinfos.size(); ++i) {
        make_music(musicinfos[i]);
    }
    
    stable_sort(music.begin(), music.end(), [](auto& a, auto& b) {
        return get<2>(a) > get<2>(b);
    });

    for (auto e : music) {
        if (is_match(get<1>(e), m)) {
            return get<0>(e);
        }
    }
    return "(None)";
}

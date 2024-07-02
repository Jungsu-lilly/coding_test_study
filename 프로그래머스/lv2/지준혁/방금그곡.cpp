#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <iostream>

using namespace std;

vector<pair<string, string>> music;

bool is_match(string& a, string& b) {
    if (a.length() < b.length()) return false;
    
    for (int i = 0; i < a.length() - b.length(); ++i) {
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
    
    int st_h, st_m, en_h, en_m;
    string title_content, title, content;
    char colon, comma;
    istringstream iss(m);
    iss >> st_h >> colon >> st_m >> comma >> en_h >> colon >> en_m >> comma >> title_content;
    size_t pos = title_content.find(',');
    title = title_content.substr(0, pos);
    content = title_content.substr(pos + 1);
    
    int playing = (en_h * 60 + en_m) - (st_h * 60 + st_m);
    string gasa = "";
    int idx = 0;
    while (playing) {
        gasa += content[(idx % content.length())];
        --playing;
        ++idx;
    }
    music.push_back({title, gasa});
}

string solution(string m, vector<string> musicinfos) {
    
    for (int i = 0; i < musicinfos.size(); ++i) {
        make_music(musicinfos[i]);
    }
    
    sort(music.begin(), music.end(), [](auto& a, auto& b) {
        return a.second.size() > b.second.size();
    });

    for (auto e : music) {
        if (is_match(e.second, m)) {
            return e.first;
        }
    }
    return "(None)";
}

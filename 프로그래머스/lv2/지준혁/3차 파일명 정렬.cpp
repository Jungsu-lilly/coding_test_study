#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

// 실패

vector<tuple<string, string, int>> f; // head, number, turn

void detach(int index, string& file_name) {
    
    string h = "";
    int i = 0;
    for (; i < file_name.length(); ++i) {
        if (file_name[i] >= '0' && file_name[i] <= '9') {
            break;
        }
        if (file_name[i] >= 'A' && file_name[i] <= 'Z') {
            h += file_name[i] - 'A' + 'a';
            continue;
        }  
        h += file_name[i];
    }
    string n = "";
    for (; i < file_name.length(); ++i) {
        if (!(file_name[i] >= '0' && file_name[i] <= '9')) break;
        if (n.length() >= 5) break;
        n += file_name[i];
    }
    f.push_back({h, n, index});
}

vector<string> solution(vector<string> files) {
    
    for (int i = 0; i < files.size(); ++i) {
        detach(i, files[i]);
    }
    
    sort(f.begin(), f.end(), [](auto& a, auto& b) {
        string h1 = get<0>(a);
        string h2 = get<0>(b);

        int n1 = stoi(get<1>(a));
        int n2 = stoi(get<1>(b));
        if (h1 == h2) {
            return n1 < n2;
        } else {
            return h1 < h2;
        }
    });
    
    vector<string> ans;
    for (auto e : f) {
        ans.push_back(files[get<2>(e)]);
    }
    return ans;
}

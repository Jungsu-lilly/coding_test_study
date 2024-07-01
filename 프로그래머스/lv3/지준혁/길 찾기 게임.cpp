#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <tuple>

using namespace std;

int lc[10'004];
int rc[10'004];

void setParent(int pa_idx, int ch_idx, int ch_x, vector<vector<int>>& nodeinfo) {
    
    int pa_x = nodeinfo[pa_idx - 1][0];
        
    if (ch_x < pa_x) {
        if (lc[pa_idx] == 0) {
            lc[pa_idx] = ch_idx;
        } 
        else {
            setParent(lc[pa_idx], ch_idx, ch_x, nodeinfo);
        }
    } else {
        if (rc[pa_idx] == 0) {
            rc[pa_idx] = ch_idx;
        } 
        else {
            setParent(rc[pa_idx], ch_idx, ch_x, nodeinfo);
        }
    }
}

void preorder(int idx, vector<int>& ret) {
    if (idx == 0) return;
    
    ret.push_back(idx);
    preorder(lc[idx], ret);
    preorder(rc[idx], ret);
}

void postorder(int idx, vector<int>& ret) {
    if (idx == 0) return;
    
    postorder(lc[idx], ret);
    postorder(rc[idx], ret);
    ret.push_back(idx);
}

vector<vector<int>> solution(vector<vector<int>> nodeinfo) {
    vector<tuple<int, int, int>> nodes;

    for (int i = 0; i < nodeinfo.size(); ++i) {
        nodes.push_back({i + 1, nodeinfo[i][0], nodeinfo[i][1]});
    }

    sort(nodes.begin(), nodes.end(), [](auto& a, auto& b) {
        if (get<2>(a) != get<2>(b)) {
            return get<2>(a) > get<2>(b);
        }
        return get<1>(a) < get<1>(b);
    });

    
    int root_idx = get<0>(nodes[0]);
    for (int i = 1; i < nodes.size(); ++i) {
        setParent(root_idx, get<0>(nodes[i]), get<1>(nodes[i]), nodeinfo);
    }

    vector<vector<int>> ans;
    vector<int> pre, post;
    
    preorder(root_idx, pre);
    postorder(root_idx, post);

    ans.push_back(pre);
    ans.push_back(post);

    return ans;
}

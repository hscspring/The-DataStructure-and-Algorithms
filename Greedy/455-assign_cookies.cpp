#include <vector>
#include <iostream>

using namespace std;

int findContentChildren(vector<int>& g, vector<int>& s) {
    sort(g.begin(), g.end());
    sort(s.begin(), s.end());
    int i = 0, j = 0;
    while (i < g.size() && j < s.size()) {
        if (g[i] <= s[j]) {
            i++;
        }
        j++;
    }
    return i;
}


int main() {
    vector<int> s = {1, 2, 3};
    vector<int> g = {1, 2};
    int res = findContentChildren(g, s);
    cout << res << endl;
    return 0;
}

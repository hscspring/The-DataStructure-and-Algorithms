#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <map>

using namespace std;


vector<int> partitionLabels(string S) {
    map<char, int> last;
    vector<int> ans;
    int size = S.size();
    for (int i=0; i<size; i++) {
        last[S[i]] = i;
    }

    int j=0, anchor=0;
    for (int i=0; i<size; i++) {
        j = max(last.at(S[i]), j);
        if (i == j) {
            ans.push_back(i-anchor+1);
            anchor = i+1;
        }
    }
    return ans;
}



int main() {
    string s = "ababcbacadefegdehijhklij";
    vector<int> res = partitionLabels(s);
    for (int i=0; i<res.size(); i++) {
        cout << res[i] << " ";
    }
    return 0;
}

#include <string>
#include <iostream>
#include <vector>

using namespace std;


class Solution {
public:
    string findLongestWord(string s, vector<string>& d) {
        sort(d.begin(), d.end(), [](string &d1, string &d2) {
            return d1.size() > d2.size() || (d1.size() == d2.size() && d1 < d2);
        });
        for (auto ss: d) {
            int i = 0;
            int size = ss.size();
            for (auto c: s) {
                if (i < size && c == ss[i]) {
                    i++;
                }
                if (i == size) {
                    return ss;
                }
            }
        }
        return "";
    }
};

int main(int argc, char* argv[]) {
    Solution so = Solution();
    string s = "abpcplea";
    vector<string> d = {"ale", "apple", "monkey", "plea"};
    string res = so.findLongestWord(s, d);
    cout << res << endl;
}

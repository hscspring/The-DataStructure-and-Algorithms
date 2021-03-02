#include <vector>
#include <iostream>
#include <algorithm>
#include <map>

using namespace std;

vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
    sort(people.begin(), people.end(), [](vector<int>& p1, vector<int>& p2) {
        return p1[0] > p2[0] || (p1[0] == p2[0] && p1[1] < p2[1]);
    });
    vector<vector<int>> result;
    for (auto p: people) {
        result.insert(result.begin() + p[1], p);
    }
    return result;
}


int main() {
    vector<vector<int>> people = {{7,0}, {4,4}, {7,1}, {5,0}, {6,1}, {5,2}};
    vector<vector<int>> res = reconstructQueue(people);
    for (int i = 0; i < res.size(); i++) {
        cout << res[i][0] << " " << res[i][1] << endl; 
    }
    return 0;
}

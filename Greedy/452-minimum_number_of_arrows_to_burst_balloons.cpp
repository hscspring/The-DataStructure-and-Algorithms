#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;


int findMinArrowShots(vector<vector<int>>& points) {
    int size = points.size();
    if (size < 2) {
        return size;
    }
    sort(points.begin(), points.end(), [](vector<int>& a, vector<int>& b) {
        return a[1] < b[1];
    });
    int total=1, prev=points[0][1];
    for (int i=1; i<size; i++) {
        if (points[i][0] <= prev) {
            continue;
        }
        total++;
        prev = points[i][1];
    }
    return total;
}



int main() {
    vector<vector<int>> points = {{10,16}, {2,8}, {1,6}, {7,12}};
    int res = findMinArrowShots(points);
    cout << res << endl;

    return 0;
}

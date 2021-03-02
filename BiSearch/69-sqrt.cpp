#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;


int mySqrt(int x) {

    if (x <= 1) {
        return x;
    }
    int l=1, r=x;
    while (l <= r) {
        int mid = l + (r - l) / 2;
        int val = x / mid;
        if (val > mid) {
            l = mid + 1;
        } else if (val < mid) {
            r = mid - 1;
        } else if (val == mid) {
            return mid;
        }
    }
    return r;
}



int main() {
    vector<int> xs = {4, 8, 10};
    for (auto x: xs) {
        int res = mySqrt(x);
        cout << res << endl;
    }

    return 0;
}

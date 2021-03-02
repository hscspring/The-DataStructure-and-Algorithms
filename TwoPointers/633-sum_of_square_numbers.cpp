#include <vector>
#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;


bool judgeSquareSum(int c) {
    if (c < 0) {
        return false;
    }
    long int l = 0, r = sqrt(c);
    while (l <= r) {
        long int v = l*l + r*r;
        if (v < c) {
            l++;
        } else if (v > c) {
            r--;
        } else {
            return true;
        }
    }
    return false;
}



int main() {
    bool res = judgeSquareSum(5);

    cout << res << endl;

    return 0;
}

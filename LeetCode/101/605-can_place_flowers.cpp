#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;


bool canPlaceFlowers(vector<int>& flowered, int n) {
    int i=0, total=0;
    int size = flowered.size();
    while (i < size) {
        if (flowered[i] == 0 && (i == 0 || flowered[i-1] == 0) && (i == size-1 || flowered[i+1] == 0)) {
            flowered[i] = 1;
            total++;
        }
        if (total >=n ) {
            return true;
        }
        i++;
    }
    return false;
}



int main() {
    vector<int> flowered = {1, 0, 0, 0, 1};
    int n = 1;
    bool res = canPlaceFlowers(flowered, n);
    cout << res << endl;

    return 0;
}

#include <vector>
#include <iostream>
#include <algorithm>
#include <numeric>

using namespace std;


int candy(vector<int>& ratings) {
    int size = ratings.size();
    if (size < 2) {
        return size;
    }
    vector<int> nums(size, 1);
    for (int i=1; i < size; i++) {
        if (ratings[i] > ratings[i-1]) {
            nums[i] = nums[i-1] + 1;
        }
    }

    for (int i=size - 1; i > 0; i--) {
        if (ratings[i] < ratings[i-1]) {
            nums[i-1] = max(nums[i-1], nums[i]+1);
        }
    }
    return accumulate(nums.begin(), nums.end(), 0);
}


int main() {

    vector<int> ratings = {1, 0, 2};
    int res = candy(ratings);
    cout << res << endl;
    return 0;
}

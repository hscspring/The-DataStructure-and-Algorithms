#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;


bool checkPossibility(vector<int>& nums) {
    int cnt = 0;
    for (int i=1; i<nums.size() & cnt <= 1; i++) {
        if (nums[i-1] > nums[i]) {
            cnt++;
            if (i == 1 || nums[i-2] <= nums[i]) {
                nums[i-1] = nums[i];
            } else {
                nums[i] = nums[i-1];
            }
        }
    }
    return cnt <= 1;
}



int main() {
    vector<int> nums = {3, 4, 2, 3};
    bool res = checkPossibility(nums);
    cout << res << endl;
    return 0;
}

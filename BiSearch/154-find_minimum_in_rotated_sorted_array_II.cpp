#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;


int findMin(vector<int>& nums) {
    int l=0, r=nums.size()-1;
    while (l <= r) {
        int mid = l + (r - l ) / 2;
        if (nums[mid] > nums[r]) {
            l = mid + 1;
        } else if (nums[mid] < nums[r]) {
            r = mid;
        } else {
            --r;
        }
    }
    return nums[l];
}



int main() {
    vector<int> nums = {3, 1, 3};
    int res = findMin(nums);
    cout << res << endl;
    return 0;
}

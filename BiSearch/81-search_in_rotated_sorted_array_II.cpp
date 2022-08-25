#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;


bool search(vector<int>& nums, int target) {
    int l=0, r=nums.size()-1;
    while (l <= r) {
        int mid = l + (r - l) / 2;
        int val = nums[mid];
        int begin = nums[l];
        int end = nums[r];
        if (val == target) {
            return true;
        }
        if (begin == target) {
            ++l;
        } else if (val <= end) {
            if (target > val && target <= end) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
            
        } else {
            if (target < val && target >= begin) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
    }
    return false;
}



int main() {

    vector<int> nums = {2, 5, 6, 0, 0, 1, 2};
    int target = 0;
    target = 3;
    bool res = search(nums, target);
    cout << res << endl;

    return 0;
}

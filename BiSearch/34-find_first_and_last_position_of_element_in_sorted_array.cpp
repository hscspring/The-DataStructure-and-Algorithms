#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;


int bound(vector<int>& nums, int target, bool left)
{
    int l=0, r=nums.size() - 1;
    while (l <= r) {
        int mid = l + (r - l ) / 2;
        int val = nums[mid];
        if (val > target) {
            r = mid - 1;
        } else if (val < target) {
            l = mid + 1;
        } else if (val == target) {
            if (left) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
    }
    if (left) return l;
    else return r;
}


vector<int> searchRange(vector<int>& nums, int target) 
{
    int l = bound(nums, target, true);
    int r = bound(nums, target, false);
    if (l <= r) return vector<int>{l, r};
    else return vector<int>{-1, -1};

}




int main() {
    vector<int> nums = {5, 7, 7, 8, 8, 10};
    int target = 8;
    vector<int> res = searchRange(nums, target);
    cout << res[0] << " " << res[1] << endl;

    return 0;
}

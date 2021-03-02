#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;


vector<int> twoSum(vector<int>& nums, int target) {
    int l=0, r=nums.size() - 1;
    while (l < r) {
        int sum = nums[l] + nums[r];
        if (sum == target) break;
        else if (sum > target) r--;
        else l++;
    }
    return vector<int> {l+1, r+1};

}



int main() {

    vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    vector<int> res = twoSum(nums, target);

    cout << res[0] << " " << res[1] << endl;

    return 0;
}

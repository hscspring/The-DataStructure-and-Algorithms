#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

void show(vector<int>& nums) {
    for (auto v: nums) {
        cout << v << " ";
    }
    cout << endl;
}

void merge(vector<int>& nums, int l, int m, int r) {
    int n1 = m - l + 1;
    int n2 = r - m;
    vector<int> ln(n1);
    vector<int> rn(n2);
    for (int i=0; i<n1; i++) {
        ln[i] = nums[l+i];
    }
    for (int j=0; j<n2; j++) {
        rn[j] = nums[m+1+j];
    }
    int k=l, i=0, j=0;
    while (i < n1 || j < n2) {
        if (j >= n2 || (i < n1 && ln[i] <= rn[j])) {
            nums[k] = ln[i];
            i++;
        } else {
            nums[k] = rn[j];
            j++;
        }
        k++;
    }
}


void merge_sort(vector<int>& nums, int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;
        merge_sort(nums, l, m);
        merge_sort(nums, m+1, r);
        merge(nums, l, m, r);
    }
}



int main() {
    vector<int> nums = {1, 2, 3, 3, 3, 3, 3, 4, 5, 3, 3, 2, 1};
    merge_sort(nums, 0, nums.size() - 1);
    show(nums);

    return 0;
}

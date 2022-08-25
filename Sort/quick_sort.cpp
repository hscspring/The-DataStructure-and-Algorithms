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

int partition1(vector<int>& nums, int l, int r) {
    int pivot = nums[r];
    int i=l;
    for (int j=l; j<r; j++) {
        if (nums[j] < pivot) {
            swap(nums[i], nums[j]);
            i++;
        }
    }
    swap(nums[i], nums[r]);
    return i;
}


void quick_sort1(vector<int>& nums, int l, int r) {
    if (l < r) {
        int p = partition1(nums, l, r);
        quick_sort1(nums, l, p - 1);
        quick_sort1(nums, p + 1, r);
    }
}


int partition(vector<int>& nums, int l, int r) {
    int mid = l + (r - l) / 2;
    int pivot = nums[mid];
    while (l <= r) {
        while (nums[l] < pivot) {
            l++;
        }
        while (nums[r] > pivot) {
            r--;
        }
        if (l <= r) {
            swap(nums[l], nums[r]);
            l++;
            r--;
        }
    }
    return l;
}

void quick_sort(vector<int>& nums, int l, int r) {
    if (l < r) {
        int p = partition(nums, l, r);
        quick_sort(nums, l, p - 1);
        quick_sort(nums, p,  r);
    }
}



int main() {
    vector<int> nums = {1, 2, 3, 3, 3, 3, 3, 4, 5, 3, 3, 2, 1};
    quick_sort(nums, 0, nums.size() - 1);
    show(nums);

    vector<int> nums1 = {1, 3, 5, 7, 2, 6, 0, 9, 9 , 7, 3, 1};
    quick_sort1(nums1, 0, nums1.size() - 1);
    show(nums1);

    vector<int> nums2 = {1, 3, 5, 7, 2, 6, 0, 9, 9 , 7, 3, 5};
    int p2 = partition1(nums2, 0, nums2.size() - 1);
    cout << p2 << endl;
    show(nums2);
    return 0;
}

#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;


void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
    int pos = m-- + n-- - 1;
    while (m >=0 & n >=0) {
        nums1[pos--] = nums1[m] > nums2[n] ? nums1[m--]: nums2[n--];
    }
    while (n >=0 ) {
        nums1[pos--] = nums2[n--];
    }
}



int main() {
    vector<int> nums1 = { 1, 2, 3, 0, 0, 0 };
    int m = 3;
    vector<int> nums2 = { 2, 5, 6 };
    int n = 3;
    merge(nums1, m, nums2, n);
    for (int i=0; i<nums1.size(); i++) {
        cout << nums1[i] << endl;
    }
    return 0;
}

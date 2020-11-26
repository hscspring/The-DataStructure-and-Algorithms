#include <iostream>
#include <vector>

using namespace std;

int biSearch(vector<int> v, int target)
{
    int a = 0, b = v.size();
    while (a < b) {
        int k = (a + b) / 2;
        if (v[k] == target) {
            return k;
        }
        if (v[k] > target) b = k-1;
        else a = k+1;
    }
    return -1;
}


int findingSmallest(vector<int> v) {
    int x = -1;
    for (int b=v.size()-1; b >=1; b /= 2) {
        while (!v[x+b]) {
            cout << "x: " << x << endl;
            cout << "b: " << b << endl;
            x += b;
        }
    }
    int k = x + 1;
    return k;
}


int findingMaximum(vector<int> v) {
    int x = -1;
    for (int b=v.size()-1; b >=1; b /= 2) {
        while (v[x+b] < v[x+b+1]) {
            x += b;
        }
    }
    int k = x + 1;
    return k;
}


int main() {
    vector<int> v = {8};
    int idx = biSearch(v, 8);
    cout << idx << '\n';
    int idx2 = biSearch(v, 10);
    cout << idx2 << '\n';

    vector<int> v2 = {1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 10};
    auto r = equal_range(v2.begin(), v2.begin()+10, 5);
    cout << r.second - r.first << '\n';

    vector<int> v3 = {0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1};
    int k = findingSmallest(v3);
    cout << k << '\n';

    vector<int> v4 = {1, 2, 3, 4, 5, 4, 3, 2, 0};
    int idx3 = findingMaximum(v4);
    cout << idx3 << '\n';
}

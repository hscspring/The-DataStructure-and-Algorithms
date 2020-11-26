#include <iostream>
#include <vector>

using namespace std;

struct P {
    int x, y;
    bool operator<(const P &p) {
        if (x != p.x) return x < p.x;
        else return y < p.y;
    }
};

int main()
{
    vector<int> v  = {4, 2, 5, 3, 5, 8, 3};
    sort(v.begin(), v.end());
    
    cout << "Hello";
    for (int i=0; i<v.size(); i++) {
        cout << v[i] << ' ';
    };

    int n = 7;
    int a[] = {4, 2, 5, 3, 5, 8, 3};
    sort(a, a+n);
    for (int j=0; j<n; j++) {
        cout << a[j] << ' ';
    };

    vector<pair<int, int>> vp;
    vp.push_back({1, 5});
    vp.push_back({2, 3});
    vp.push_back({1, 2});
    sort(vp.begin(), vp.end());

    for (int k=0; k<vp.size(); k++) {
        cout << vp[k].first << " " << vp[k].second << endl;
    };

    struct P p1 = {1, 2};
    struct P p2 = {0, 1};

    bool is_small = p1 < p2;
    cout << is_small << endl;

}



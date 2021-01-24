#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <random>
#include <set>
#include <bitset>


using namespace std;

int main() {

    vector<int> v = {3, 4, 6, 5, 1, 2};

    sort(v.begin(), v.end());
    reverse(v.begin(), v.end());
    shuffle(v.begin(), v.end(), random_device());

    for (auto i: v) {
        cout << i << " ";
    }

    sort(v.begin(), v.begin()+3);


    cout << "\n";
    for (auto i: v) {
        cout << i << " ";
    }

    set<int> s;
    s.insert(3);
    s.insert(5);
    s.insert(2);

    cout << "\n";

    for (auto it = s.begin(); it != s.end(); it++) {
        cout << *it << "\n";
    }

    auto it = s.end(); 
    it--;
    cout << *it << "\n";
    cout << "\n";

    {
       set<int> s; 
       s.insert(3);
       s.insert(5);
       s.insert(2);
       s.insert(6);
       s.insert(1);
       int x = 9;
       auto ib = s.begin();
       cout << "begin: " << *ib << "\n";
       auto ie = s.end(); ie--;
       cout << "end: " << *ie << "\n";

       auto it = s.lower_bound(x);
       if (it == s.begin()) {
           cout << *it << "\n";
       } else if (it == s.end()) {
           it--;
           cout << *it << "\n";
       } else {
           int a = *it;
           it--;
           int b = *it;
           if (x-b < a-x) cout << b << "\n";
           else cout << a << "\n";
       }

    }

    bitset<10> bs(string("0010011010"));
    cout << bs[4] << "\n";

    bitset<10> a(string("0010110110"));
    bitset<10> b(string("1011011000"));
    cout << (a&b) << "\n";


    return -1;
}

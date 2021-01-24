#include <iostream>
#include <string>
#include <vector>


using namespace std;

vector<int> subset;
int n = 3;

void search(int k) {
    cout << "k: " << k << "\n";
    if (k==n) {
        for (auto i: subset) {
            cout << i << " ";
        }
        cout << "\n";
        return;
    } else {
        // search(k+1);
        subset.push_back(k);
        search(k+1);
        subset.pop_back();
    }
}


int main() {
    
    search(0);
    return 0;
}

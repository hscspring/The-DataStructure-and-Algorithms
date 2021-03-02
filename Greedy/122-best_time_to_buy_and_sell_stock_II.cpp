#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;


int maxProfit(vector<int>& prices) {
    int total = 0;
    for (int i=1; i<prices.size(); i++) {
        if (prices[i] > prices[i-1]) {
            total += prices[i] - prices[i-1];
        }
    }
    return total;
}



int main() {
    vector<int> prices = {1, 7, 2, 3, 6, 7, 6, 7};
    int res = maxProfit(prices);
    cout << res << endl;
    return 0;
}

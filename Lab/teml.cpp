/*
ID: haoshao1
LANG: C++
PROG: ride
*/

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>

using namespace std;

int  main() {
    string line;
    ofstream fout ("test.out");
    ifstream fin ("test.in");

    if (fin.is_open()) {
        while (getline (fin, line)) {
            cout << line << '\n';
        }
        fin.close();
    }

    return 0;
}

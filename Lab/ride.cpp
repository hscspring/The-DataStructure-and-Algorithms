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
    string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    map<char, int> dict;
    for (int i = 0; i < alphabet.length(); i++) {
        dict[alphabet[i]] = i+1;
    }

    ofstream fout ("ride.out");
    ifstream fin ("ride.in");
    string comet, group;
    fin >> comet >> group;
    int comet_v = 1;
    int group_v = 1;
    int v;
    for(char c: comet) {
        comet_v *= dict[c];
    }
    for(char c: group) {
        group_v *= dict[c];
    }

    if (comet_v % 47 == group_v % 47) {
        fout <<  "GO" << endl;
    } else {
        fout <<  "STAY" << endl;
    }
    return 0;
}

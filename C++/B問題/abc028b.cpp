#include <bits/stdc++.h>
using namespace std;

int main() {
    string s = "";
    cin >> s;
    vector<int> a(6);
    for(int i = 0;i<6;i++){
        a.at(i) = count(s.begin(),s.end(),'A'+i);
    }
    for(int i = 0;i<5;i++){
        cout << a.at(i) << " ";
    }
    cout << a.at(5) << endl;
    return 0;
}
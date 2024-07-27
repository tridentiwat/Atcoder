#include <bits/stdc++.h>
using namespace std;

int main() {
    string a[15] = {};
    for(int i = 0;i<15;i++){
        cin >> a[i];
    }
    sort(begin(a), end(a));
    cout << a[6] << endl;
}

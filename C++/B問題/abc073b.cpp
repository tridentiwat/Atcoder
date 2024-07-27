#include <bits/stdc++.h>
using namespace std;

int main() {
    int n=0,l=0,r=0,people = 0;
    cin >> n;
    for(int i = 0;i<n;i++){
        cin >> l >> r;
        people = people +  r - l + 1;
    }
    cout << people << endl;
    return 0;
}
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n=0,study=0,a=0;
    cin >> n;
    for(int i = 0 ;i<n;i++){
        cin >> a;
        if(a<80){
            study = study + 80 - a;
        }
    }
    cout << study << endl;
    return 0;
}
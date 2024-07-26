#include <bits/stdc++.h>
using namespace std;

int main() {
    int n,d,x,day,j=0,a,chocolate=0;
    cin >>n;
    cin >>d>>x;
    for(int i = 0;i<n;i++){
        cin >> a;
        j = 0;
        day = a*j+1;
        while(day<=d){
            chocolate += 1;
            j += 1;
            day = a*j+1;
        }
    }
    cout << chocolate+x << endl;
    return 0;
}
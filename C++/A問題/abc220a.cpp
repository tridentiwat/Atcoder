#include <bits/stdc++.h>
using namespace std;

int main() {
    int a,b,c,ans,i=1;
    bool exists = false;
    cin >> a >> b >> c;
    ans = c*i;
    
    while(ans <= b){
        if(ans >= a){
            exists = true;
            break;
        }
        i += 1;
        ans = c * i;
    }
    if(exists){
        cout<< ans << endl;
    }else{
        cout << -1 << endl;
    }
}
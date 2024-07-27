#include <bits/stdc++.h>
using namespace std;

int main() {
    int l=0,h=0,n=0,a=0;
    cin >> l >> h >> n;
    int ans[n] = {};
    for(int i=0;i<n;i++){
        cin >> a;
        if(a >= l && a<=h){
            ans[i] = 0;
        }else if(a < l){
            ans[i] = l - a;
        }else{
            ans[i] = -1;
        }
    }
    for(int i = 0;i<n;i++){
        cout<<ans[i]<<endl;
    }
    return 0;
}
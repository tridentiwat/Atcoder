#include <bits/stdc++.h>
using namespace std;

int sm(int);
int main() {
int n,a,b,answer=0,sum=0;
cin >> n >> a >> b;
    for(int i = 1;i<=n;i++){
        sum = sm(i);
        if(sum >= a){
            if(sum <= b){
                answer = answer + i;
            }
        }
    }
    cout << answer << endl;
    return 0;
}
int sm(int n){
    int sum = 0;
    while(n){
        sum += n%10;
        n = n/10;
    }
    return sum;
}
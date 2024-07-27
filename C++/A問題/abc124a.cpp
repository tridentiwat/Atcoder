#include <bits/stdc++.h>
using namespace std;

int main() {
int a,b,answer=0;
cin >> a >> b;
for(int i = 0;i<2;i++){
    if(a >= b){
        answer += a;
        a += -1;
    }else{
        answer += b;
        b += -1;
    }
}
cout<<answer<<endl;
return 0;
}

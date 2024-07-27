#include <bits/stdc++.h>
using namespace std;

int main() {
int a,b;
cin >> a >> b;
int plus = a+b,minus = a-b,mul = a*b;
if(plus >= minus && plus >= mul){
    cout << plus << endl;
}else if(minus >= plus && minus >= mul){
    cout << minus << endl;
}else{
    cout << mul << endl;
}
}
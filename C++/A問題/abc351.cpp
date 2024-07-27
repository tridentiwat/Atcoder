#include <bits/stdc++.h>
using namespace std;

int main() {
int a,Takahashi=0,Aoki=0;
for(int i = 0;i<9;i++){
    cin >> a;
    Takahashi += a;
}
for(int i = 0;i<8;i++){
    cin >> a;
    Aoki += a;
}
cout <<(Takahashi-Aoki)+1<< endl;
}
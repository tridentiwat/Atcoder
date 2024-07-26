#include <bits/stdc++.h>
using namespace std;

int main() {
int marble = 0;
string s;
cin >> s;
for(int i = 0;i<3;i++){
    if(s[i] == '1'){
        marble = marble + 1;
    }
}
cout << marble << endl;
return 0;
}
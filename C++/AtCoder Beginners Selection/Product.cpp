#include <bits/stdc++.h>
using namespace std;

int main() {
    int a,b;
    cin >> a >> b;
    if((a*b)%2==0){
        cout << "Even" << endl;
    }else{
        cout << "Odd" << endl;
    }
}
/*
#include <bits/stdc++.h>とusing namespace std;は毎回最初に書く
C++のプログラムはmain関数から始まる
cout << "文字列" << endl;で文字列を出力できる
*/
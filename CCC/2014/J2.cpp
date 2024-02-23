//
#include <iostream>
#include <string>

using namespace std;
int main(){
    int a = 0;
    int b = 0;
    int n;
    cin >> n;
    string s;
    cin >> s;
    for (int y = 0; y < n; y++){
        if (s[y] == 'A'){
            a++;
        }
        else{
            b++;
        }
    }
    if (a > b){
        cout << 'A' << '\n';
    }
    else{
        if (b > a){
            cout << 'B' << '\n';
        }
        else{
            cout << "Tie" << '\n';
        }
    }
    return 0;
}
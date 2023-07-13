#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n;
    cin >> n;

    for(int i = 2; i < 20; i++) {
        if (n % i) {
            for(int j = 0; j < n/i; j++) {
                for(int k =0; k < i; k++) {
                    cout << char(k + 'a');
                }
            }

            for(int j = 0; j < n % i; j++) {
                cout << char(j + 'a');
            }cout << '\n';
            return;
        }
    }



    return;
}

int main(){
    ios::sync_with_stdio(false);cin.tie(0);

    int t;
    cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}

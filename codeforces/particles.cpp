#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n;
    cin >> n;
    vector<long long> vec(n);
    long long mx = LLONG_MIN;
    for (int i = 0; i < n; i++) {
        cin >> vec[i];
        mx = max(mx, vec[i]);
    }
    if (mx <= 0) {
        cout << mx << endl;
        return;
    }
    long long res = mx;
    long long sm = 0;
    for (int i = 0; i < n; i += 2) {
        if (vec[i] >= 0)
            sm += vec[i];
    }
    res = max(res, sm);
    sm = 0;
    for (int i = 1; i < n; i += 2)
        if (vec[i] >= 0)
            sm += vec[i];
    cout << max(res, sm) << endl;
    return;
}

int32_t main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int t;
  cin >> t;
  while (t--) {
    solve();
  }
  return 0;
}

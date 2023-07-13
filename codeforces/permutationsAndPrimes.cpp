#include <iostream>
#include <vector>
using namespace std;

int main() {
  long long t;
  cin >> t;
  while (t--) {
    long long n;
    cin >> n;
    vector<long long> a(n);
    a[0] = 2;
    a[n - 1] = 3;
    a[n / 2] = 1;
    long long count = 4;
    for (int i = 1; i < n - 1; i++) {
      if (i == n / 2)
        continue;
      a[i] = count++;
    }
    for (int i = 0; i < n; i++) {
      cout << a[i] << " ";
    }
    cout << endl;
  }
  return 0;
}

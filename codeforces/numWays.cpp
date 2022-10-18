#include <cstdio>
#include <vector>
using namespace std;
int main() {
  int n;
  scanf("%d", &n);
  vector<long long> sum(n + 1, 0);
  for (int i = 1; i <= n; i++) {
    int element_i;
    scanf("%d", &element_i);

    sum[i] = sum[i - 1] + element_i;
  }
  vector<long long> sum_from(n + 1, 0);
  for (int i = 1; i <= n; i++) {
    sum_from[i] = sum[n] - sum[i - 1];
  }
  long long num = 0, total = sum[n];
  if (total % 3 != 0) {
    printf("%lld\n", num);
    return 0;
  }
  vector<int> third(n + 2, 0);
  for (int i = n; i >= 1; i--) {
    third[i] = third[i + 1] + (3 * sum_from[i] == total);
  }
  for (int i = 1; i <= n - 2; i++) {
    if (3 * sum[i] == total) {
      num += third[i + 2];
    }
  }
  printf("%lld\n", num);
  return 0;
}

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main () {
  int N;
  cin >> N;
  std::vector<int> L;
  for (auto i = 0; i < N; ++i){
    int l;
    cin >> l;
    L.push_back(l);
  }
  
  std::sort(L.begin(), L.end());

  auto num_triangle = 0;

  for (auto i = N-1; i > 1; --i){
    auto a = L[i];
    for (auto j = i-1; j > 0; --j){
      auto b = L[j];
      auto c = L[j-1];
      if (a >= b+c){ break; }
      num_triangle += j - distance(L.begin(), upper_bound(L.begin(), L.begin()+j, a-b));
    }
  }

  cout << num_triangle << endl;

  return 0;
}

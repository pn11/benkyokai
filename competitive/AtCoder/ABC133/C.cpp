#include <iostream>
using namespace std;
typedef long long ll;

int main(){
	ll L, R;
    cin >> L >> R;

    ll minimum = 2019;
  
   	for (ll i = L; i <= R-1; ++i){
        for (ll j = L+1; j <= R; ++j){
            ll mod = (i*j) % 2019;
            minimum = min(mod, minimum);
            
            if (minimum == 0){
                cout << minimum << endl;
                return 0;
            }
        }
    }
  
    cout << minimum << endl;
    return 0;
}

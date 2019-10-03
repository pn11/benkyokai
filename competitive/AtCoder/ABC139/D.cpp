#include <iostream>
#include <cstdlib>
using namespace std;

int main(){
    long N;

    cin >> N;

    long long ans = 0;

    for (auto i = 1; i <= N-1; i++){
        ans += i;
    }
    cout << ans << endl;
}

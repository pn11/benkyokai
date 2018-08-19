// TLE

#include <iostream>
using namespace std;

int main()
{
    long N, M;

    cin >> N;
    cin >> M;

    long long *cumA = new long long[N + 1];

    long long A;
    long long cum = 0;
    cumA[0] = 0;

    for (int i = 1; i < N+1; ++i)
    {
        cin >> A;
        cum += A;
        cumA[i] = cum;
    }
  
    int num = 0;

    for (int i = 0; i < N+1; ++i)
    {
        for (int j = i+1; j < N+1; ++j)
        {
            if ((cumA[j] - cumA[i]) % M == 0)
            {
                num += 1;
            }
        }
    }

    cout << num << endl;
    return 0;
}

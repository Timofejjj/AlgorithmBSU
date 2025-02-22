#include <iostream>
#include <vector>
using namespace std;

const int MOD = 1000000007;

long long modExp(long long base, long long exp) {
    long long result = 1;

    while(exp > 0) {
        if(exp & 1)
            result = (result * base) % MOD;
        base = (base * base) % MOD;
        exp >>= 1;
    }
    return result;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    cin >> n >> k;

    if(k > n - k) {
        k = n - k;
    }

    vector<long long> fact(n + 1, 0), inv_fact(n + 1, 0);

    fact[0] = 1;
    for (int i = 1; i <= n; i++) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }

    /////
    inv_fact[n] = modExp(fact[n], MOD - 2);

    for (int i = n - 1; i >= 0; i--) {
        inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD;
    }

    /////
    long long ans = (fact[n] * inv_fact[k]) % MOD;
    ans = (ans * inv_fact[n - k]) % MOD;
    cout << ans;

    return 0;
}

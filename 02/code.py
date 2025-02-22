import sys
import numpy as np

def modExp(base, exp):
    result = 1
    while exp > 0:
        if exp & 1:
            result = (result * base) % (10**9 + 7)
        base = (base * base) % (10**9 + 7)
        exp //= 2
    return result


n, k = map(int, input().split())

if k > n - k:
    k = n - k

fact = np.zeros(n + 1, dtype=np.int64)
inv_fact = np.zeros(n + 1, dtype=np.int64)

##
fact[0] = 1
for i in range(1, n + 1):
    fact[i] = (fact[i - 1] * i) % (10**9 + 7)

##
inv_fact[n] = modExp(int(fact[n]), (10**9 + 7) - 2)
for i in range(n - 1, -1, -1):
    inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % (10**9 + 7)

#
ans = (fact[n] * inv_fact[k]) % (10**9 + 7)
ans = (ans * inv_fact[n - k]) % (10**9 + 7)

print(ans)

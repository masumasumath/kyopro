def eratosthenes_sieve(n):
    is_prime = [True]*(n + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, n + 1):
        if is_prime[p]:
            for q in range(2*p, n + 1, p):
                is_prime[q] = False
    return is_prime

N = int(input())
for i in range(2, int(N**(1/2))):
    if i**3 > N//2:
        break
ubound = i**3
counti = 0
countj = 0
tmpi = 0
tmpj = 0
for i in range(2,ubound + 1):
    tmpi += 1
    if not eratosthenes_sieve(i): continue
    for j in range(j,ubound + 1):
        if not eratosthenes_sieve(j): continue
        tmpj += 1
        if i * j**3 < N: continue
    counti += tmpi
    countj += tmpj
    tmpi, tmpj = 0, 0

print(counti* countj)
    

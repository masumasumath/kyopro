N,M,K = map(int,input().split())
mod = 998244353
ans = 1
for i in range(N):
    ans *=( (M-2*K)*( M-2*K-1 )%mod  + K*(M-2*K-1)+K*(K+1)//2 )%mod
print(ans%mod)




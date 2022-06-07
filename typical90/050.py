mod = 10**9 + 7
N, L = map(int,input().split())
if L > N:
    print(1)
    exit()
    
dp = [0 for _ in range(N+1)]

#初期化
for i in range(L): dp[i] = 1

for i in range(L,N+1): dp[i] = (dp[i-1] + dp[i-L]) % mod

print(dp[N]%mod)

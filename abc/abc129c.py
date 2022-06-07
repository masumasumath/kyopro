mod = 1000000007
N, M = map(int, input().split())
A = set(int(input()) for _ in range(M))

if N == 1:
    print(1)
    exit()


dp = [0] * (N+1)
dp[0] = 1
if 1 in A:
    dp[1] = 0
else:
    dp[1] = 1

if 2 in A:
    dp[2] = 0
else:
    dp[2] = dp[1] + 1

for i in range(N-1):
    if i+2 not in A:
        dp[i+2] = (dp[i+1] + dp[i])%mod
print(dp[N])
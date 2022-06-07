from matplotlib.colors import ListedColormap

mod = 10**9 + 7

N = int(input())
P = []

for _ in range(N):
    A = list(map(int,input().split()))
    P.append(sum(A))

ans = 1
for p in P: ans = (ans*p)%mod
print(ans)
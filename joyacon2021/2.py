N = int(input())
K = int(input())
X = list(map(int,input().split()))
ans = 0
#(X[i],i)にボールがある
for i in range(N):
    if abs(K-X[i]) < abs(X[i]):
        ans += 2*abs(K-X[i])
    else:
        ans += 2*abs(X[i])
print(ans)
        


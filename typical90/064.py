N,Q = map(int,input().split())
A = list(map(int,input().split()))
huben = []
ans = 0
for i in range(N-1):
    huben.append(A[i+1]-A[i])
    ans += abs(A[i+1]-A[i])

for _ in range(Q):
    l,r,v = map(int,input().split())
    if l > 1:
        ans -= abs(huben[l-2])
        huben[l-2] += v
        ans += abs(huben[l-2])
        #dl1 = abs(A[l-1] - A[l-2])
        #dl2 = abs(A[l-1]+v-A[l-2])
    if r < N:
        ans -= abs(huben[r-1])
        huben[r-1] -= v
        ans += abs(huben[r-1])
        #dr1 = abs(A[r-1] - A[r])
        #dr2 = abs(A[r-1]+v-A[r])
    print(ans)


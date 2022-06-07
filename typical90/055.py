N,P,Q = map(int,input().split())
A = list(map(lambda x: x%P, list(map(int,input().split()))))
ans = 0
for i in range(N):
    r = A[i]%P
    for j in range(i+1,N):
        rr = r*A[j] % P
        for k in range(j+1,N):
            rrr = rr*A[k] % P
            for l in range(k+1, N):
                rrrr = rrr*A[l] % P
                for m in range(l+1, N):
                    rrrrr = rrrr*A[m] % P
                    if rrrrr == Q:ans += 1

print(ans)

A,B,C,K = map(int,input().split())
ans = 0
if A >= K:
    ans = K
elif A+B >= K:
    ans = A
else:
    ans = A-(K-(A+B))
print(ans)
    
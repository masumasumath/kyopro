N,A,B =map(int,input().split())
if A > B:
    ans = 0
elif N == 1:
    if A == B: ans = 1
    else: ans = 0
else:
    ma = B*(N-1) + A
    mi = A*(N-1) + B
    ans = ma-mi + 1
print(ans)
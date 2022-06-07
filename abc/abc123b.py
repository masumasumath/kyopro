A  = [ int(input()) for _ in range(5)]
mini = A[0]%10
idx = 0
for i, a in enumerate(A):
    if a%10 > 0 and mini > a%10:
        idx = i
ans = 0
for i, a in enumerate(A):
    if i == idx: continue
    ans += 1
    for i in range(1,14):
        if a > 10*i:
            ans += 1
print(10*ans + A[idx])
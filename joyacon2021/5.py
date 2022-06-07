N = int(input())
A = list(map(int,input().split()))
ma = max(A)
sec = 0
for i in range(N):
    if sec < A[i] < ma:
        sec = A[i]
        ans = i+1
    
print(ans)



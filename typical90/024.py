N, K =map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
#AとBの差の絶対値の合計
diff = 0
for i in range(N):
    diff += abs(A[i]-B[i])
print("Yes") if diff <= K and abs(diff-K)%2 == 0 else print("No")
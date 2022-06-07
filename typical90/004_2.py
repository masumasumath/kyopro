H,W = map(int,input().split())
#列和
sumH = [0 for _ in range(W)]
#行和
sumW = []
A = []
for _ in range(H):
    a = list(map(int,input().split()))
    A.append(a)
    sumW.append(sum(a))
for i in range(W):
    for a in A:
        sumH[i] += a[i]

for i in range(H):
    for j in range(W):
        print(sumW[i] + sumH[j] - A[i][j], end = " ")
    print()

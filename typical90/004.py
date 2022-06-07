H, W = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H)]
#SUMI[i]:第i行の和
SUMI =  [0] * H
#SUMJ[j]:第j列の和
SUMJ =  [0] * W
for i in range(H):
    for j in range(W):
        SUMI[i] += A[i][j]

for i in range(H):
    for j in range(W):
        SUMJ[j] += A[i][j]

for i in range(H):
    for j in range(W):
        print(SUMI[i]+SUMJ[j]-A[i][j], end=' ')
    print()

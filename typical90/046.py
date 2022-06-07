from matplotlib.colors import ListedColormap


N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

for i in range(N):
    A[i] %= 46
    B[i] %= 46
    C[i] %= 46
cntA = [0 for i in range(46)]
cntB = [0 for i in range(46)]
cntC = [0 for i in range(46)]
for i in range(N):
    cntA[A[i]%46] += 1
    cntB[B[i]%46] += 1
    cntC[C[i]%46] += 1

ans = 0
for i in range(46):
    for j in range(46):
        for k in range(46):
            if (i+j+k)%46 == 0:
                ans += cntA[i] * cntB[j] * cntC[k]
print(ans)
    

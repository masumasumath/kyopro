N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
EX = 0
for i in range(N):
    EX += A[i]/3 + B[i]*2/3
print(EX)
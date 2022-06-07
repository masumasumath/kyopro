N = int(input())
B = list(map(int,input().split()))
R = list(map(int,input().split()))

ExB = 0
ExR = 0
for i in range(N):
    ExB += B[i]
    ExR += R[i]
ExB /= N
ExR /= N
print(ExB+ExR)
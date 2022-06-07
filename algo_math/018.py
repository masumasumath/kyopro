N = int(input())
A = list(map(int,input().split()))

CNT = [0] * 4
for a in A: CNT[a//100 - 1] += 1
print(CNT[0]*CNT[3] + CNT[1]*CNT[2])
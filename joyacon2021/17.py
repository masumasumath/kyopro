N = int(input())
A = list(map(int,input().split()))
ANS = [0 for i in range(N+1)]
for a in A:ANS[a] += 1
for i in range(1,N+1):
    print(ANS[i])
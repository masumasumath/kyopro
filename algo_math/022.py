N = int(input())
A = list(map(int,input().split()))

CNT = [0] * (500000)
for a in A: CNT[a] += 1

ans = 0
target = 100000
for i in range(50000):
    ans += CNT[i]*CNT[target-i]
ans += CNT[50000]*(CNT[50000]-1)//2
print(ans)
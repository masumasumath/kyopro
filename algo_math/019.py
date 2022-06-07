N = int(input())
A = list(map(int,input().split()))
CNT = [0] * 3
for a in A: CNT[a-1] += 1
ans = sum(map(lambda c: c*(c-1)//2, CNT ))
print(ans)
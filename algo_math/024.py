N = int(input())
EX = 0
for _ in range(N):
    p,q = map(int,input().split())
    EX += q/p
print(EX)

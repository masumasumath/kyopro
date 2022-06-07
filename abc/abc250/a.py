H,W = map(int,input().split())
R,C = map(int,input().split())

ans = 0
for x in range(1,H+1):
    for y in range(1,W+1):
        if abs(R-x) + abs(C-y) == 1:ans += 1
print(ans)
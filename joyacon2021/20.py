
N = int(input())
S = []
setS = set()
for _ in range(N):
    s = input()
    S.append(s)
    setS.add(s)
M = int(input())
T = []
for _ in range(M):
    T.append(input())
pt = 0
ans = 0
for s in setS:
    pt = S.count(s) - T.count(s)
    ans = max(ans,pt)
print(ans)
from collections import deque

N, M = map(int,input().split())
G = [[] for _ in range(N+1)]
P = [ [ False ] * (N+1) for _ in range(N+1)]
for i in range(1,N+1):
    P[i][i] = True
for _ in range(M):
    a, b = map(int,input().split())
    G[a].append(b)

for i in range(1,N+1):
    Q = deque(G[i])
    while Q:
        q = Q.popleft()
        if not P[i][q]:
            P[i][q] = True
            Q.extend(G[q])

ans = sum(map(lambda p: p.count(True), P))
print(ans)
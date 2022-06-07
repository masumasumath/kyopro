N, M = map(int,input().split())
NODE = [[] for _ in range(N+1)]
#ans[x,y]:x小さい頂点の個数，y,リセットしたかどうか
cnt = [[0,1] for _ in range(N+1)]
for i in range(1,M+1):
    a,b =map(int,input().split())
    NODE[a].append(b)
    NODE[b].append(a)
    t = max(a,b)
    if cnt[t][0] == 0:
        cnt[t][0] += 1
    else:
        cnt[t][1] = 0
ans = 0
for c in cnt:
    ans += c[0]*c[1]
print(ans)
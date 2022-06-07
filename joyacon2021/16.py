import itertools
N,K = map(int,input().split())
#T[i][j]にiからjにかかる時間を格納
T = []
for i in range(N):
    t = list(map(int,input().split()))
    T.append(t)
ans = 0
root = [ i for i in range(1,N)]
for iter in itertools.permutations(root,N-1):
    time = 0
    now = 0
    for it in iter:
        time += T[now][it]
        now = it
    time += T[it][0]
    if time == K: ans += 1
print(ans)


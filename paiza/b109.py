def distance(x,y,p,q):
    return abs(x-p) + abs(y-q)

N,H,W,p,q = map(int,input().split())
reserved = []
for _ in range(N):
    l = list(map(int,input().split()))
    reserved.append(l)

min_d = H*W
for h in range(H):
    for w in range(W):
        if [h,w] in reserved:
            continue
        d = distance(h,w,p,q)
        if min_d > d: min_d = d

for h in range(H):
    for w in range(W):
        if distance(h,w,p,q) == min_d and [h,w] not in reserved:print(h,w)



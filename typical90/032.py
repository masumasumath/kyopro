import itertools

N = int(input())
A = []
for _ in range(N):
    a = list(map(int,input().split()))
    A.append(a)
M = int(input())
NG =[set() for _ in range(N)]
for _ in range(M):
    x,y = map(int,input().split())
    NG[x-1].add(y-1)
    NG[y-1].add(x-1)

if N == 1:
    print(A[0][0])
    exit()
    
time = 0
ans = 10000
#オーダーを全探索
for order in itertools.permutations(range(N),N):
    order = iter(order)
    kukan = 0

    #pは今の走者
    p = next(order)
    while kukan < N:
        
        #qは次の走者
        if kukan < N-1 :
            q = next(order)
            #pとqの受け渡しができない場合はなし
            if p in NG[q]:
                time = 0
                break
        #pがkukanを走るときにかかる時間を加算
        time += A[p][kukan]
        
        #次の区間に進める
        kukan += 1
        p = q

    if time > 0:
        ans = min(ans,time)
        time = 0

print(ans) if ans != 10000 else print(-1)
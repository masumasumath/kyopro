N = int(input())
RES = []
for i in range(N):
    s,p = input().split()
    RES.append([s,int(p),i+1])
while 1:
    flg = False
    for i in range(N-1):
        if RES[i][0] > RES[i+1][0]:
            RES[i],RES[i+1] = RES[i+1], RES[i]
            flg = True
        if RES[i][0] == RES[i+1][0] and RES[i][1] < RES[i+1][1]:
            RES[i],RES[i+1] = RES[i+1], RES[i]
            flg = True
    if not flg: break
for res in RES:
    print(res[2])

            
Q = int(input())
lis1 = []
lis2 = []

for _ in range(Q):
    t,x = map(int,input().split())
    if t == 1:
        lis1.append(x)
    elif t == 2:
        lis2.append(x)
    elif t == 3:
        if x <= len(lis1):
            print(lis1[-x])
        else:
            print(lis2[x-len(lis1)-1])

N,A,B = map(int,input().split())
tile = [[-1] * (N*B) for _ in range(N*A)]
for i in range(N*A):
    for j in range(N*B):
        x = i//A
        y = j//B
        if tile[i][j] == -1:
            if (x+y)%2 == 0:
                tile[i][j] = "."
            else:
                tile[i][j] = "#"
for ti in tile:
    for t in ti:
        print(t,end = "")
    print()



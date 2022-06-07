N, Q = map(int,input().split())
A = list(map(int,input().split()))
shift = 0
for _ in range(Q):
    T,x,y = map(int,input().split())
    x = (x -1 - shift)%N
    y = (y -1 - shift)%N

    #swap x y
    if T == 1:
        A[x], A[y] = A[y], A[x]
    #shift -> 
    elif T == 2:
        shift += 1
    #print Ax
    else:
        print(A[x])


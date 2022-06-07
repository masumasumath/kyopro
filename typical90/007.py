def binary(l,r,b):
    while r - l > 1:
        m = (r+l)//2
        if A[m] == b:
            return m
        if A[m] < b:
            l = m
        elif b < A[m]:
            r = m
    return l

N = int(input())
A = list(map(int,input().split()))
A.sort()

Q = int(input())
if N == 1:
    for _ in range(Q):
        print(abs(A[0]-int(input())))
else:
    for _ in range(Q):
        b = int(input())
        t = binary(0,N-1,b)
        ans = min(abs(A[t]-b), abs(A[t+1]-b))
        print(ans)

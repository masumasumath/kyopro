def gcd(x,y):
    while 0 not in [x,y]:
        if x < y: x, y = y,x
        x = x%y
    return max(x,y)


N = int(input())
A = list(map(int,input().split()))
A.sort()

r = gcd(A[0],A[1])
for i in range(2,N):
    r = gcd(r,A[i])
print(r)


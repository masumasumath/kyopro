def gcd(x,y):
    while 0 not in [x,y]:
        if x < y: x,y = y,x
        x = x%y
    return max(x,y)

def lcm(x,y):
    g = gcd(x,y)
    return x*y//g


N = int(input())
A = list(map(int,input().split()))
m = lcm(A[0],A[1])
for i in range(2,N):
    m = lcm(m,A[i])
print(m)
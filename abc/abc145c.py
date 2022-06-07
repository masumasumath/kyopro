import itertools

def length(x0,y0, x1,y1):
    return ( (x0-x1)**2 + (y0-y1)**2 ) ** 0.5

def factorial(n):
    if n == 1: return 1
    return n*factorial(n-1)

N = int(input())
XY = [ list(map(int,input().split())) for _ in range(N)]
total = 0
for C in itertools.permutations(XY):
    for i in range(N-1):
        total += length(C[i][0],C[i][1],C[i+1][0],C[i+1][1])

print(total/factorial(N))


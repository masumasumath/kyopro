def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y,x%y)

def lcm(x,y):
    return x*y//gcd(x,y)

N,A,B = map(int,input().split())
cntA = N//A
cntB = N//B
g = gcd(A,B)
l = lcm(A,B)
cntAB = N//l

print(N*(N+1)//2 - A*cntA*(cntA+1)//2 - B*cntB*(cntB+1)//2 + l*cntAB*(cntAB+1)//2)



def gcd2(x,y):
    if y == 0: return x
    return gcd2(y,x%y)

def gcd3(a,b,c):
    m = gcd2(a,b)
    return gcd2(m,c)

A,B,C = map(int,input().split())
g = gcd3(A,B,C)
print(A//g + B//g + C//g -3)
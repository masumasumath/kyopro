def gcd(x,y):
    if y == 0: return x
    return gcd(y,x%y)

def lcm(x,y):
    return x*y//gcd(x,y)

A,B = map(int,input().split())
ans = lcm(A,B)
if ans > 10**18:
    print("Large")
else:
    print(ans)
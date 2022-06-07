def factorize(n):
    if n == 1: return 1
    else: return n*factorize(n-1)

n,r = map(int,input().split())
if n == r:
    ans = 1
else:
    ans = factorize(n)//(factorize(n-r)*factorize(r))
print(ans)
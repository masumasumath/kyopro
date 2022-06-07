x,y = map(int,input().split())
ans = 0
if x == y:
    ans = x
else:
    ans = 3-(x+y)
print(ans)


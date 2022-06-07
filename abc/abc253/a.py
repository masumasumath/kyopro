a,b,c = map(int,input().split())
mx = max(a,b,c)
mn = min(a,b,c)
medi = a+b+c - mx -mn
if medi == b:
    print("Yes")
else:
    print("No")
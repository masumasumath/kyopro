N = int(input())
if N%1000 == 0:
    ans = 0
else:
    ans = 1000-N%1000
print(ans)
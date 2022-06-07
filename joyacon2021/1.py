N = int(input())
L = list(map(int,input().split()))
maxL = max(L)
if sum(L)-maxL > maxL:
    ans = 'Yes'
else:
    ans = 'No'
print(ans)

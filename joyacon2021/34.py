a,b = input().split()
ab = int(a+b)
ans = 'No'
for i in range(1,1000):
    if i*i == ab:ans = 'Yes'
print(ans)
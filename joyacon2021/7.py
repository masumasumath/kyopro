A = list(map(int,input().split()))
isSeven = 0
isFive = 0
for i in range(3):
    if A[i] == 7:
        isSeven += 1
    if A[i] == 5:
        isFive += 1
if isSeven == 1 and isFive == 2:
    ans = 'YES'
else:
    ans = 'NO'
print(ans)
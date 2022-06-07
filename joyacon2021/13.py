N = int(input())
D = [] * N
for _ in range(N):
    d = list(map(int,input().split()))
    D.append(d)
ans = 'No'
flg = False
for i in range(N-2):
    for j in range(3):
        if D[i+j][0] == D[i+j][1]:
            flg = True
            continue
        else:
            flg = False
            break
    if flg:
        ans = 'Yes'
        break
print(ans)
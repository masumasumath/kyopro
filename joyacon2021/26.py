S = input()
tmp = 0
ans = 0
target = ['A','G','C','T']
for i in range(len(S)):
    if S[i] in target:
        tmp += 1
        ans = max(tmp,ans)
    else:
        tmp = 0
print(ans)


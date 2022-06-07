S = input()
T = 'oxx'*(10**5)
ans = 'No'
for i in range(len(T)-len(S)+1):
    if S == T[i:i+len(S)]:
        ans = 'Yes'
print(ans)
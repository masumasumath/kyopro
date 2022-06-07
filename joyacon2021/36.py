S = input()
T = input()
if S==T:
    ans = 'Yes'
else:
    S = list(S)
    ans = 'No'
    for i in range(len(S)):
        L = list(S[:len(S)-1])
        S = S[-1] + "".join(L)
        if S == T:
            ans = 'Yes'
            break
        S = list(S)
print(ans)
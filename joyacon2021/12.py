S = input()
if len(S) <= 1:
    print(0)
    exit()
i = 0
ans = 0
while i < len(S)-1:
    if S[i] != S[i+1]:
        S = S[:i]+S[i+2:]
        ans += 2
        if i > 0: i -= 1
        continue
    i += 1
print(ans)
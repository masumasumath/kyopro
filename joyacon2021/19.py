s = input()
ans = 0
for i in range(len(s)):
    if s[i] == 'C':
        ans = 1
    if ans == 1 and s[i] == 'F':
        ans = 2
        break
if ans == 2:
    print('Yes')
else:
    print('No')
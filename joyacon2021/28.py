A,B,C,D = map(int,input().split())
if A+B > C+D:
    ans = 'Left'
elif A+B < C+D:
    ans = 'Right'
else:
    ans = 'Balanced'
print(ans)

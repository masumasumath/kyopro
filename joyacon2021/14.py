K = int(input())
A,B = map(int,input().split())
SA = str(A)
SB = str(B)
ka = 0
for i in range(len(SA)):
    ka += int(SA[i])*(K**(len(SA)-i-1))
kb = 0
for i in range(len(SB)):
    kb += int(SB[i])*(K**(len(SB)-i-1))
print(ka*kb)

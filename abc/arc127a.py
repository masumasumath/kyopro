N = int(input())
#lはNの桁数
K = len(str(N))

sumf = 0
for i in range(K-1,0,-1):
    sumf += i*9*10**(K-1-i)
sumf += K
#N以下で最大の11....111
for j in range(N,min(N,2*10**(K-1))):
    s = str(j)
    idx = 0
    while idx < len(s) and s[idx] == 1:
        sumf += 1
print(sumf)



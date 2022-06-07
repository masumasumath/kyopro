N = int(input())
t = 1
for i in range(2,int(N**0.5) + 1):
    if N%i == 0:
        t = i
print((t-1) + N//t -1)


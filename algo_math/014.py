N = int(input())

i = 2
while i*i <= N:
    if N%i == 0:
        print(i, end=' ')
        N //= i
    else:
        i += 1
print(N)
    
    
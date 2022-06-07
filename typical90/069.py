mod = 10**9 + 7

N, K = map(int,input().split())

KK = K*(K-1)%mod

if N == 1:
    print(K)
elif K >= 3:
    #print( KK * (pow((K-2),(N-2))%mod)%mod )
    print( KK * (pow((K-2),(N-2),mod))%mod )
elif K == 2:
    if N <= 2:
        print(2)
    else:
        print(0)
elif K == 1:
    print(0)


N, W = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
setAns = set()

for i in range(N):
    if A[i] <= W:
        setAns.add(A[i])
    else:
        break
    for j in range(i+1,N):
        if A[i] + A[j] <= W:
            setAns.add(A[i]+A[j])
        else:
            break
        for k in range(j+1,N):
            if A[i]+A[j]+A[k] <= W:
                setAns.add(A[i]+A[j]+A[k])
            else:
                break

print(len(setAns))


    

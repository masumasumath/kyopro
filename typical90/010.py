N = int(input())
score1 = [0 for _ in range(N+1)]
score2 = [0 for _ in range(N+1)]
for i in range(1,N+1):
    c,p = map(int,input().split())
    if c == 1:
        score1[i] = p
        score2[i] = 0
    else:
        score1[i] = 0
        score2[i] = p

cumsum1 = [0 for _ in range(N+1)]
cumsum2 = [0 for _ in range(N+1)]
for i in range(1,N+1):
    cumsum1[i] = cumsum1[i-1] + score1[i]
    cumsum2[i] = cumsum2[i-1] + score2[i]
 
Q = int(input())
for _ in range(Q):
    l,r = map(int,input().split())
    print(cumsum1[r]-cumsum1[l-1], cumsum2[r]- cumsum2[l-1])


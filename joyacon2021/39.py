N,Q = map(int,input().split())
S = input()
#CNT[index]:indexまでに何個の'AC'が含まれるか
#区間[l,r]に含まれる'AC'の個数はCNT[r]-CNT[l-1]となる
CNT = [0] * N
for r in range(N-1):
    if S[r:r+2] == 'AC':
        CNT[r+1] = CNT[r] + 1
    else:
        CNT[r+1] = CNT[r]
for _ in range(Q):
    l,r = map(int,input().split())
    print(CNT[r-1]-CNT[l-1])

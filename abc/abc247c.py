N = int(input())
S = ["0","1"]
for i in range(1,N):
    S.append(S[i]+" "+str(i+1)+" "+S[i])
print(S[N])

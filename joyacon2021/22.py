from operator import itemgetter
def getNo(a):
    noA = 0
    no = 0
    for i in range(len(a)):
        no += noX[a[i]]*(100**(maxLen-i))
    return no


X = input()
noX = {}
#各アルファベットが何番目かを格納
for i in range(26):noX[X[i]] = i+1

N = int(input())
S = []
dic = {}
maxLen = 0
for _ in range(N):
    s = input()
    S.append(s)
    maxLen = max(len(s),maxLen)
for i in range(N):
    dic[S[i]] = getNo(S[i])
LIS = list(dic.items())
LIS.sort(key=lambda x:x[1])

for ans in LIS:print(ans[0])

N = int(input())
S = [input() for _ in range(N)]
dic = {}
for s in S:
    if s in dic.keys():
        t = dic[s]
        dic[s] = t+1
    else:
        dic[s] = 1
ANS = list(dic.items())
ANS.sort(key = lambda x:x[1])
print(ANS[-1][0])
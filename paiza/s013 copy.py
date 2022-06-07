import queue
from sys import breakpointhook
#時代の数
N = int(input())
#未来へ行くコスト，過去へ行くコスト
c_f,c_b = map(int,input().split())
#どの世代が安全か危険か
#s:安全，d:危険
A = input()
OKNG = ["*"]
for a in A:
    if a == "s":OKNG.append(True)
    else:OKNG.append(False)
COST = 0
ANS = 100*(N**7)
RT = []

q = queue.Queue()
q.put(N)

while len(q) > 0:
    now = q.get()
    #次に行ける場所をqueに格納する
    for i, go in OKNG:
        if i == 0:continue
        if go:
            COST
            q.put(i)

    

    




print(RT)

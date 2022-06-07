import itertools
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


ERA = list(itertools.permutations(range(1,N+1)))

for era in ERA:
    cnt = 0
    #最後にNに帰るものだけ考える
    if era[-1] != N:continue
    now = N
    for nxt in era:
        #行ける（安全）
        if OKNG[nxt]:
            if nxt < now: COST += c_b
            else: COST += c_f
            for j in range(nxt+1,len(OKNG)):
                if OKNG[j]: OKNG[j] = False
                else:OKNG[j] = True
            now = nxt
        #いけない場合は3度だけ2回目の訪問をする
        else:
            flg = False
            break

    if flg:
        #COSTが過去最小であれば，ルートを更新する
        if COST < ANS:
            RT = [N] + list(era)
            ANS = COST

    #次のループのために初期化
    COST = 0
    for k,a in enumerate(A):
        if a == "s":OKNG[k+1] = True
        else:OKNG[k+1] = False   
    flg = True 
print(RT)

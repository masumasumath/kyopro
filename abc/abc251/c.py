N = int(input())
sub = []
moji = set()
#何番目か，得点
yusho = [-1,-1]
for i in range(N):
    s,t = input().split()
    #オリジナルかどうか
    if s in moji:
        flg = 0
    else:
        flg = 1
        moji.add(s)
    if flg:
        t = int(t)
        #得点が高い
        if yusho[1] < t:
            yusho = [i+1,t]
print(yusho[0])

    

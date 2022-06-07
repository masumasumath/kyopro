N,Q = map(int,input().split())

#i番目に何が書かれているか
BALL = [0] + [i for i in range(1,N+1)]
#iが書かれたボールがどこにあるか
WHERE =[0] + [i for i in range(1,N+1)]

for _ in range(Q):
    x = int(input())

    #xが一番右にあるとき
    if WHERE[x] == N:
        placeL = WHERE[x]
        valueR = BALL[WHERE[x]-1]

        #ボールの入れ替え
        BALL[WHERE[x]],BALL[WHERE[x]-1] = BALL[WHERE[x]-1],BALL[WHERE[x]]
        #ボールの場所の管理の修正
        WHERE[x] -= 1
        WHERE[valueR] = placeL

    else:
        placeL = WHERE[x]
        valueR = BALL[WHERE[x] + 1]

        #ボールの入れ替え
        BALL[WHERE[x]],BALL[WHERE[x]+1] = BALL[WHERE[x]+1],BALL[WHERE[x]]

        #ボールの場所の管理の修正
        WHERE[x] += 1
        WHERE[valueR] = placeL
    
print(*BALL[1:])
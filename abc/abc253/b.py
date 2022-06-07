H, W  =map(int,input().split())
S = []
sX,sY = -1,-1
gX,gY = -1,-1
cnt = 0
for i in range(H):
    s = input()
    S.append(s)
    for j in range(W):
        if s[j] == "o" and cnt == 0:
            sX = i
            sY = j
            cnt += 1
        if s[j] == "o" and cnt == 1:
            gX = i
            gY = j

print(abs(sX-gX) + abs(sY-gY))


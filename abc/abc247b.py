N = int(input())
NAME = []

for _ in range(N):
    s,t = input().split()
    NAME.append([s,t])

for i in range(len(NAME)):
    flg1, flg2 = True, True
    s = NAME[i][0]
    t = NAME[i][1]
    for j in range(len(NAME)):
        if i == j: continue
        if flg1 and s != NAME[j][0] and s != NAME[j][1]:
            flg1 = True
        else:
            flg1 = False
            
        if flg2 and t != NAME[j][0] and t != NAME[j][1]:
            flg2 = True
        else:
            flg2 = False
    if not( flg1 or flg2 ):break
        
print("Yes") if flg1 and flg2 else print("No")


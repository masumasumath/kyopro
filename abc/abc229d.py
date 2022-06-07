S = input()
N = len(S)
K = int(input())
#cntX[i]はi文字目までにXが何個出現しているか
#cntX[j]-cntX[i] + 1は区間[i,j]におけるXの個数
#cntX[j]-cntX[i] + 1 <= Kのとき，区間[i,j]をすべてXにすることができる（j-i+1個のX）
cntX = [0] * (N+1)
for i in range(1,N+1):
    if S[i-1] == 'X':
        cntX[i] = cntX[i-1] + 1
    else:
        cntX[i] = cntX[i-1]


right = 0
ans = 0
for left in range(N+1):
    #(left-right) - (cntX[right]- cntX[left])は[left, r)に含まれる.の数
    while right < N+1 and (right-left) - (cntX[right]- cntX[left]) <= K:
        ans = max(ans, right - left)
        right += 1
    if left == right: right += 1
print(ans)






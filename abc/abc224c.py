import itertools

N = int(input())
XY = [list(map(int,input().split())) for _ in range(N)]

# ans = 0
# for p in itertools.combinations(XY, 3):
#     p1 = list(p)[0]
#     p2 = list(p)[1]
#     p3 = list(p)[2]
#     if (p1[1]-p2[1])*(p1[0]-p3[0]) != (p1[1]-p3[1])*(p1[0]-p2[0]):
#         ans += 1
# print(ans)

ans = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1, N):
            if (XY[i][1]-XY[j][1])* (XY[i][0] -XY[k][0]) != (XY[i][1]-XY[k][1])* (XY[i][0] -XY[j][0]):
                ans += 1
print(ans)


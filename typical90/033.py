H,W = map(int,input().split())
ans = 0
if H == 1 or W == 1:
    print(H*W)
    exit()

# for i in range(W):
#     for j in range(H):
#         if i%2 == 0 and j%2 == 0:
#             ans += 1

print((H+1)//2 * (W+1)//2)

# print(ans)

W,H,N = map(int,input().split())
w = 0
h = 0
for _ in range(N):
    x,y,a = map(int,input().split())
    #xより左を塗る
    if a == 1: w = max(x,w)
    #xより右を塗る
    if a == 2: W = min(x,W)
    #yより下を塗る
    if a == 3: h = max(y,h)
    #yより上を塗る
    if a == 4: H = min(y,H)
print( max( max( (W-w),0 ) * max( (H-h),0 ), 0))
import heapq

N,K = map(int,input().split())
score = []
for _ in range(N):
    #a:得点，b:部分点
    a,b = map(int,input().split())
    score.append([-b,-(a-b)])
heapq.heapify(score)
ans = 0
for i in range(K):
    t = heapq.heappop(score)
    ans += -t[0]
    heapq.heappush(score,[t[1],0])

print(ans)
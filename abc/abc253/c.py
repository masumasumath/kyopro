import heapq
q1 = []
q2 = []
heapq.heapify(q1)
heapq.heapify(q2)

S = dict()
setS = set()

Q = int(input())
for _ in range(Q):
    query = input().split()
    qtype = query[0]
    if qtype == "1":
        x = int(query[1])
        if x in S.keys():
            S[x] += 1
        else:
            S[x] = 1

        if S[x] == 1:
            heapq.heappush(q1,-x)
            heapq.heappush(q2,x)

    if qtype == "2":
        x, c = int(query[1]),int(query[2])
        if x in S.keys():
            S[x] = max(0, S[x]-c)

    if qtype == "3":

        mx = -heapq.heappop(q1)
        while S[mx] == 0:
            mx = -heapq.heappop(q1)

        mn = heapq.heappop(q2)
        while S[mn] == 0:
            mn = heapq.heappop(q2)

        print(mx-mn)
        heapq.heappush(q1,-mx)
        heapq.heappush(q2,mn)

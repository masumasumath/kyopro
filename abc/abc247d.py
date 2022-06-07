Q = int(input())
space = []
head = 0

for _ in range(Q):
    query_type, *query = input().split()
    if query_type == "1":
        x = int(query[0])
        c = int(query[1])
        space.append([x,c])

    if query_type == "2":
        res = 0
        c = int(query[0])
        #t[0]:なんの数字か，t[1]:いくつ保存されているか
        t = space[head]
        while t[1] <= c:
            res += t[0] * t[1]
            c -= t[1]
            head += 1
            if head < len(space):t = space[head]
        #保存されている個数が十分多い場合
        if t[1] > c:
            res += t[0]*c
            t[1] -= c
        print(res)
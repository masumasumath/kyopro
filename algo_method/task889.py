X = int(input())
Q = int(input())
task = []
head = 0
tail =0
cnt = 0
out = 0
qq = []
for _ in range(Q):
    q = list(map(int,input().split()))
    qq.append(q)

for q in qq:
    query_type = q[0]
    t = q[1]
    #t = int(t)
    #push
    #taskの割り当て
    if query_type == 0:
        #時刻tで開始
        task.append(t)
    #pop
    #完了したtaskの個数を出力
    else:
        while head < len(task) and task[head] < t-X:
            head += 1 
            cnt += 1
        print(cnt)
        


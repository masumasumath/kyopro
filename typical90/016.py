N = int(input())
A,B,C = map(int,input().split())
first = max(A,B,C)
third = min(A,B,C)
second = A+B+C-first-third
ans = 9999

for i in range(10000):
    if first*i > N:break
    if first*i == N:
        if ans > i: ans = i
    for j in range(10000-i):
        if first*i + second*j > N: break
        if first*i + second*j == N:
            if ans > i+j: ans = i+j
        elif (N - (first*i + second*j))%third == 0 and (N - (first*i + second*j))//third > 0:
            if ans > i+j+(N - (first*i + second*j))//third:
                ans = i+j+(N - (first*i + second*j))//third
print(ans)
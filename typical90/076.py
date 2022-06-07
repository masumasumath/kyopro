N = int(input())
A = list(map(int,input().split()))

area = sum(A)
A =  A + A

ans = "No"
part = 0
l, r = 0, 0
while l < N:
    while 10*part < area:
        part += A[r]
        r += 1
    if 10*part == area:
        ans = "Yes"
        break
    part -= A[l]
    l += 1
print(ans)

N, K = map(int,input().split())
A = list(map(int,input().split()))
ma = max(A)
B = list(map(int,input().split()))
for i,a in enumerate(A):
    if a == ma and i in B:
        print("Yes")
        exit()
print("No")

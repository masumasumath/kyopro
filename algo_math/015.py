A,B = map(int,input().split())

if A < B:A,B = B,A

while 0 not in [A,B]:
    if A < B:A,B = B,A
    A = A%B
print(max(A,B))
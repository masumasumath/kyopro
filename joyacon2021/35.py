N = int(input())
candidate = set()
ans = 0
for a in range(2,int(N**0.5)+1):
    for b in range(2,40):
        t = a**b
        if t <= N and t not in candidate:
            candidate.add(t)
        else:
            break
print(N-len(candidate))
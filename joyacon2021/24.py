import itertools
def isTri(l,m,n):
    return abs(m-l) < n < l+m


N = int(input())
L = list(map(int,input().split()))
ans = 0
for nums in itertools.combinations(range(N),3):
    l,m,n = L[nums[0]],L[nums[1]],L[nums[2]]
    if isTri(l,m,n) and l != m and l!= n and m != n:
        ans += 1
print(ans)


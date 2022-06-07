import itertools
S,K = input().split()
K = int(K)
setS = set()
for nums in itertools.permutations(range(len(S))):
    tmp = ''
    for i in range(len(nums)):
        tmp = tmp + S[nums[i]]
    setS.add(tmp)
ANS = list(setS)
ANS.sort()
print(ANS[K-1])


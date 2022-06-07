def manhattan():
    res = 0
    for x in X:
        res += abs(x)
    return res

def euclid():
    res = 0
    for x in X:
        res += x**2
    return res**0.5

def chebichev():
    absX = []
    for x in X:
        absX.append(abs(x))
    return max(absX)

N = int(input())
X = map(int,input().split())

man = 0
euc = 0
che = 0
for x in X:
    man += abs(x)
    euc += x**2
    che  = max(abs(x),che)
euc **= 0.5
print(man)
print(euc)
print(che)


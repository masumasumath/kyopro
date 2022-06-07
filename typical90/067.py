#base進法の数Xを10進法に変換
def ToTen(base,X):
    strX = str(X)
    digit = len(strX)
    res = 0
    for i in range(digit):
        res += int(strX[i]) * (base ** (digit-i-1))
    return res

#10進法の数Xをto進法に変換
def To(X,to):
    res = ""
    while X:
        res = str(X%to) + res
        X //= to
    return res

#N8は8進法
N8, K = map(int,input().split())
for i in range(K):
    N10 = ToTen(8,N8)
    N9 = To(N10,9)

    strN9 = str(N9)
    t = ""
    for i in range(len(strN9)):
        if strN9[i] != "8":
            t += strN9[i]
        else:
            t += "5"
    N8 =  int(t) if t != "" else  0
print(N8)
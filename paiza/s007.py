import sys
sys.setrecursionlimit(10 ** 9)

anscnt = 1
def CntAlphabet(multiple,nest,str):
    global anscnt
    anscnt += 1
    m = 1
    keta = 0
    i = 0
    while i < len(str):
        s = str[i]
        #数字のとき
        while s.isnumeric():
            keta += 1
            i += 1
            s = str[i]
        if keta > 0:
            m = int(str[i-keta:i])
            keta = 0
        if 0 <= ord(s)-97 <= 26:
            ANS[anscnt][ord(s)-97] += m
            i += 1
            m = 1
            continue
        #(のときは再帰呼び出し
        elif s == '(':
            lcnt = 1
            rcnt = 0
            k = i+1
            while lcnt != rcnt:
                if str[k] == '(': lcnt += 1
                elif str[k] == ')': rcnt += 1
                k += 1
            CntAlphabet(m,nest + 1,str[i+1:k-1])
            i = k
            m = 1
            continue
        #アルファベットをカウント
        elif 0 <= ord(s) - 97 <= 26:
            ANS[anscnt][ord(s) - 97] += 1
        i += 1
    #)のとき
    if nest == 0:
        for j in range(26):
            ANS[anscnt][0] = ANS[anscnt][j]
            ANS[anscnt][j] = 0
        return True
    else:
        for j in range(26):
            ANS[0][j] += multiple * ANS[anscnt][j]
        anscnt += 1
        return True
    

S = input()
ANS = [[0] * 26 for _ in range(1000)]
multiple = 1
nest = 0
CntAlphabet(multiple,nest,S)
for i in range(26):
    print(chr(i + 97),ANS[0][i])

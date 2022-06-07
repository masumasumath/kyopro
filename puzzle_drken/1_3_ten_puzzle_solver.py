import itertools

def calc_poland(pol):
    space = []
    for p in pol:
        if "0" <= p <= "9":
            p = int(p)
            space.append(p)
        else:   
            scd = space.pop(-1)
            fst = space.pop(-1)
            if p == "+":    
                t = fst + scd
            elif p == "-":
                t = fst - scd
            elif p == "*":
                t = fst * scd
            else:
                if scd == 0:break
                t = fst / scd
            space.append(t)
    return space[0] if len(space) > 0 else 999

def decode_poland(pol):
    space = []
    for p in pol:
        if "0" <= p <= "9":
            #p = int(p)
            space.append(p)
        else:   
            scd = space.pop(-1)
            fst = space.pop(-1)

            if p == "*" or p == "/":
                if len(fst) > 1 and ("+" in fst or "-" in fst):
                    fst = "(" + fst + ")"
                if len(scd) > 1 and ("+" in scd or "-" in scd):
                    scd = "(" + scd + ")"

            if p == "+":    
                t = fst + "+" + scd
            elif p == "-":
                t = fst + "-" + scd
            elif p == "*":
                t = fst + "*" + scd
            else:
                t = fst + "/" + scd
            space.append(t)
    return space[0]


def check(pol):
    if abs(calc_poland(pol) - target) < 1e-9:
        ANS.append(decode_poland(pol))
    

#4つの数字をスペース区切りで入力
nums = list(input().split())
#作りたい数
target = int(input())
#答えとなる数式を格納するlist
ANS = []
ops = ["+","-","*","/"]

for x in itertools.permutations(nums):
    for op1 in ops:
        for op2 in ops:
            for op3 in ops:
                #XXXX***のパターン
                ex = [ x[0],x[1],x[2],x[3],op1,op2,op3 ]
                check(ex)

                #XXX*X**のパターン
                ex = [ x[0],x[1],x[2],op1,x[3],op2,op3 ]
                check(ex)

                #XXX**X*のパターン
                ex = [ x[0],x[1],x[2],op1,op2,x[3],op3 ]
                check(ex)

                #XX*XX**のパターン
                ex = [ x[0],x[1],op1,x[2],x[3],op2,op3 ]
                check(ex)
    
                #XX*X*X*のパターン
                ex = [ x[0],x[1],op1,x[2],op2,x[3],op3 ]
                check(ex)
ANS =set(ANS)
for ans in ANS:print(ans)
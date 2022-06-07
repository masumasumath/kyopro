pol = list(input())
space = []

while pol:
    p = pol.pop(0)
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
print(space[0])

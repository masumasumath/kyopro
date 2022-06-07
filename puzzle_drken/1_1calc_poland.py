pol = list(input())
space = []

while pol:
    p = pol.pop(0)
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
            t = fst / scd
        space.append(t)
print(space[0])


N = int(input())
for i in range(2**N):
    bra = format(i,"0"+str(N)+"b")
    print(bra)
    cntl, cntr = 0, 0
    flg = True
    for b in bra:    
        if b == "0":
            cntl += 1
        else:
            cntr += 1
        if cntl < cntr:
            flg = False
    if flg and cntl == cntr and len(bra) == N:
        for b in bra:
            if b == "0":
                print("(",end="")
            else:
                print(")",end="")
        print()


S = input()
ANS = "0"
for i in range(len(S)-1):
    if S[i] == "1":
        ANS += "1"
    else:ANS += "0"
print(ANS)

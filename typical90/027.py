N = int(input())
Users = set()
for i in range(1,N+1):
    s = input()
    if not s in Users:
        Users.add(s)
        print(i)

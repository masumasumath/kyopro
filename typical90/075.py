from re import I


def factrize(n):
    rem = n
    i = 2
    cnt = 0
    while i*i <= n:
        while rem%i == 0:
            cnt += 1
            rem //= i
        i += 1
    if rem != 1: cnt += 1
    return cnt

N = int(input())
c = factrize(N)
i = 0
while 2**i < c: i += 1
print(i)
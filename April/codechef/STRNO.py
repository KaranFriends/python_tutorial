from sys import stdin,stdout
import math as mt


def kFactors(n, k):
    a = list()

    # insert all 2's in list
    while n % 2 == 0:
        a.append(2)
        n = n // 2

    for i in range(3, mt.ceil(mt.sqrt(n)), 2):
        while n % i == 0:
            n = n / i
            a.append(i)

    if n > 2:
        a.append(n)

    if len(a) < k:
        print("0")
        return
    else:
        print("1")


t = int(stdin.readline().rstrip())
while t > 0:
    # init = 2
    t -= 1
    x, k = map(int, stdin.readline().split())
    kFactors(x,k)

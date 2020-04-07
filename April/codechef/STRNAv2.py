# import matplotlib.pyplot as plt
import math


def primeFactors(n):
    li = []

    while n % 2 == 0:
        li.append(2)
        n = n / 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):

        while n % i == 0:
            li.append(i)
            n = n / i

    if n > 2:
        li.append(n)

    return set(li)


def print_factors(x):
    li = []
    for i in range(1, x + 1):
        if x % i == 0:
            li.append(i)
    return li



kk=1
ss={1 : [],2 : [],3 : [],4 : [],5 : [],6 : [],7 : [],8 : []}
for i in range(2, 100000):
    print(kk)
    kk+=1
    x = len(print_factors(i))
    k = len(primeFactors(i))
    ss[k].append(x)
    # e = ss.get(k)
    # print(e)
    # e.append(x)
    # e=set(e)
    # ss[k] = e

for i in range(1,9):
    print(sorted(set(ss.get(i))))
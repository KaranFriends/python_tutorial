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



x,y=[],[]
ss=0
for i in range(2, 1000000):
    ss=len(set(x))
    # z.append(i)
    size = len(print_factors(i))
    x.append(len(primeFactors(i)))
    rrr=set(x)
    if len(rrr) - ss == 1:
        print(size, len(rrr))
# plt.plot(x, y)
#
# # naming the x axis
# plt.xlabel('x - axis')
# # naming the y axis
# plt.ylabel('y - axis')
#
# # giving a title to my graph
# plt.title('My first graph!')
#
#
# plt.show()

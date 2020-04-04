from sys import stdin, stdout
import math


def primeFactors(n):
    # Print the number of two's that divide n
    while n % 2 == 0:
        print(2)
        n = n / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(n)) + 1, 2):

        # while i divides n , print i ad divide n
        while n % i == 0:
            print(i)
            n = n / i

            # Condition if n is a prime
    # number greater than 2
    if n > 2:
        print(n)

tt=int(stdin.readline())
while tt>0:
    tt -= 1
    print("weere",tt)
    xx,k = stdin.readline().split(" ")
    xx=int(xx)
    k=int(k)
    primeFactors(xx)

    e = set(x for tup in ([i, xx // i] for i in range(1, int(xx ** 0.5) + 1) if xx % i == 0) for x in tup)
    leen=len(e)-1
    # print(e,leen)
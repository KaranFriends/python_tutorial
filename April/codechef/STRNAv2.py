from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

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


style.use('ggplot')
fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')
x,y,z=[],[],[]
for i in range(2, 100):
    # print(i)
    # print(len(print_factors(i)), len(primeFactors(i)))
    z.append(i)
    y.append(len(print_factors(i)))
    x.append(len(primeFactors(i)))

print(x)
print(y)
print(z)
# ax1.plot_wireframe(x, y, z)
#
# # setting the labels
# ax1.set_xlabel('x-axis')
# ax1.set_ylabel('y-axis')
# ax1.set_zlabel('z-axis')
#
# plt.show()

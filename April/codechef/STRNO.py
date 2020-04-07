from sys import stdin,stdout

t = int(stdin.readline().rstrip())
while t > 0:
    init = 2
    t -= 1
    x, k = map(int, stdin.readline().split())
    # print("x ", x)
    # print("k ",k)
    init = 2**k
    # print(init)

    if x < init:
        print(0)
    else:
        print(1)

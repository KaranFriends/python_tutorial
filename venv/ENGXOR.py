from sys import stdin, stdout
t = int(stdin.readline())

while t > 0:
    t -= 1
    m, n = map(int, stdin.readline().split())
    f = [bin(int(i)).count("1") for i in stdin.readline().split()]
    odd, even = 0, 0
    p = []
    for i in range(n):
        p.append(bin(int(stdin.readline())).count("1"))

    for i in range(m):
        if f[i] % 2 == 0 :
            even += 1
        else:
            odd += 1

    for i in range(n):
        if p[i] % 2 == 0:
            print(even, odd)
        else:
            print(odd, even)



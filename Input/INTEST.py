from sys import stdin,stdout

t = int(stdin.readline())
while t > 0:
    t -= 1

    print(t)

n, k = map(int, stdin.readline().split())

count=0
for i in range(n):
    if int(stdin.readline())%k==0:
        count+=1

stdout.write(str(count))


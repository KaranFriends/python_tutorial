from sys import stdin,stdout
n, k = map(int, stdin.readline().split())
count=0
for i in range(n):
    if int(stdin.readline())%k==0:
        count+=1
stdout.write(str(count))
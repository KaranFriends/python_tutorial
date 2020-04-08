from sys import stdin,stdout
t = int(stdin.readline().rstrip())
while t > 0:
    t -= 1
    n, k = map(int, stdin.readline().split())
    e1=list(map(int, stdin.readline().split()))
    e2=list(map(int, stdin.readline().split()))
    anse1,anse2=0,0
    for i in e1:
        anse1 += i
    for j in e2:
        anse2 += j
        # print(anse1,anse2)
    # max=""
    print("C1") if anse1 == max(anse2,anse1) else print("C2")
    # print(max)
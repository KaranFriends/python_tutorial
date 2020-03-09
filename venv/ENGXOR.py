def countOne(n):
    count = 0
    while (n):
        n = n & (n - 1)
        count += 1
    # print(count)
    if (count % 2 == 0):
        return True
    else:
        return False

t = int(input())

while t > 0:
    m, n=input().split()
    m=int(m)
    n=int(n)
    f = list(map(int, input().strip().split()))[:m]
    while n>0:
        odd = 0
        even = 0
        p=int(input())
        for i in f:
            if countOne(i^p):
                even+=1
            else:
                odd+=1
        print(even.__str__()+" "+odd.__str__())
        n-=1
    t-=1
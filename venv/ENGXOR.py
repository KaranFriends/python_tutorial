def countOne(n):
    # count = 0
    if (n == 0):
        return 0

    else:
        # if last bit set add 1 else
        # add 0
        return (n & 1) + countOne(n >> 1)
    # print(count)

t = int(input())

while t > 0:
    m, n=input().split()
    m=int(m)
    n=int(n)
    f = list(map(int, input().strip().split()))[:m]
    while n > 0:
        odd = 0
        even = 0
        p=int(input())
        for i in f:
            if countOne(i+(p*(i+p))) % 2 == 0 :
                even+=1
            else:
                odd+=1
        print(even.__str__()+" "+odd.__str__())
        n-=1
    t-=1
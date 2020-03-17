t=int(input())
while t>0:
    n,q=map(int,input().split())
    a=list(map(int,input().split()))
    xxy={}
    line={}
    for i in range(1, n + 1):
        if i == n:
            slope = a[i] - a[0]
            line[i] = [slope, i, a[i], 1, a[0]]
        else:
            slope = a[i+1]-a[i]
            line[i]=[slope, i, a[i+1], i+1, a[i]]

    for i in range(1,q+1):
        xxy[i] = list(map(int,input().split()))
    count=[]
    for i in xxy:
        count[xxy.index(i)]=0
        for j in line:
            if i[3] > max( j[1], j[2]) || i[3] < min( j[1], j[2]):
                break
            elif max(i[1],i[2]) ==



    t-=1
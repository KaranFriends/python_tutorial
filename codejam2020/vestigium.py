from sys import stdin, stdout

T = int(stdin.readline())
# print(T)
ii=0
aa = [0]*T
while ii < T:
    N = int(stdin.readline())
    li = [0]*N
    row , column = 0 , 0
    trace = 0
    for i in range(N):
        e = input().split(" ")
        trace += int(e[i])
        temp=set(e)
        # print(temp)
        if N - len(temp) >0:
            row+=1
        li[i]=e
    for i in range(N):
        str=""
        for j in range(N):
            str += li[j][i] +" "
        # print(str)
        temp = set(str.rstrip().split(" "))
        # print(temp)
        if N - len(temp) > 0:
            column += 1
        # print(temp)
        aa[ii] = "Case #%d: %d %d %d" % (ii+1,trace, row, column)
    ii += 1

for i in range(T):
    print(aa[i])

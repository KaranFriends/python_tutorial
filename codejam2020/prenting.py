from sys import stdin, stdout

T = int(stdin.readline())
# print(T)
ii=0
aa = [0]*T
while ii < T:
            N = int(stdin.readline())
            li = [0]*N
            for i in range(N):
                li[i]=list(map(int,stdin.readline().rstrip().split(" ")))
                li[i].append(i)
            ans=""
            li = sorted(li, key = lambda li: (li[0], li[1]))
            # print(li)
            li[0].append("C")
            c, j = True, False
            C = li[0]
            J = [0,0,0,""]
            # print(li)
            rr = True
            for i in range(1,N):
                # print("c ", c," j ", j, li)
                if c==False and j==False:
                    li[i].append("J")
                    J=li[i]
                    j=True
                elif c== False and j==True:
                    if li[i][0] >= J[1]:
                        j=False
                        J=[0,0,0,""]

                    li[i].append("C")
                    C=li[i]
                    c=True
                elif c== True and j==False:
                    if li[i][0] >= C[1]:
                        c=False
                        C=[0,0,0,""]

                    li[i].append("J")
                    J=li[i]
                    j=True
                elif c==True and j==True:
                    if li[i][0] >= C[1] or li[i][0] >= J[1]:
                        if li[i][0] >= C[1]:
                            c=False
                            C=[0,0,0,""]
                        if li[i][0] >= J[1]:
                            j=False
                            J=[0,0,0,""]

                        if c==False:
                            li[i].append("C")
                            C = li[i]
                            c = True
                        elif j==False:
                            li[i].append("J")
                            J = li[i]
                            j = True
                    else:
                        aa[ii] = "Case #%d: IMPOSSIBLE" % (ii + 1)
                        rr=False
                        break
            li=sorted(li, key = lambda li: li[2])
            # print(li)
            if rr:
                # print(ii," test case ",li)
                for i in li:
                    ans += i[3]
                aa[ii] = "Case #%d: %s" % (ii+1, ans)
            ii += 1
            # elif li[i-1][0] == li[i][0] and (c == False or j == False) and li[i-1][0] > li[i][0]:

for i in range(T):
    print(aa[i])

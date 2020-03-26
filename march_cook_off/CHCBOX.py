from sys import stdin, stdout
t = int(input())

# type(t)
while t > 0:
    n=int(stdin.readline())
    m = stdin.readline()
    m=list(m.rstrip())
    ans=[]
    # print(m)

    for i in range(n):
        if i == 0:
            ans.append(m[i])
            continue

        if m[i] == m[i - 1]:
            continue

        if m[i]=="L" and m[i-1] =="R":
            continue
        elif m[i]=="R" and m[i-1] =="L":
            continue
        elif m[i]=="U" and m[i-1] =="D":
            continue
        elif m[i]=="D" and m[i-1] =="U":
            continue

        ans.append(m[i])

    # print(ans)

    # for i in m:
    #     if m.index(i) == 0:
    #         continue
    #     print(m[m.index(i)-1],i)
    #
    #     if i == m[m.index(i)-1]:
    #         # m=m[:int(m.index(i))] + m[int(m.index(i))+1:]
    #         # m.remove(i)
    #         print("duplicate removed")
    #
    #     # if i=="L" and m[m.index(i)+1] =="R":
    #     #     m.remove(m[m.index(i)+1])
    #     #     print("R removed")
    #     # elif i=="R" and m[m.index(i)+1] =="L":
    #     #     m.remove(m[m.index(i)+1])
    #     #     print("L removed")
    #     # elif i=="U" and m[m.index(i)+1] =="D":
    #     #     m.remove(m[m.index(i)+1])
    #     #     print("D removed")
    #     # elif i == "D" and m[m.index(i) + 1] == "U":
    #     #     m.remove(m[m.index(i) + 1])
    #     #     print("U removed")
    x,y=0,0
    for i in ans:
        if i=="L":
           x-=1
        elif i=="R":
            x+=1
        elif i=="U":
            y+=1
        elif i=="D":
            y-=1

    print(x, y)
    t-=1
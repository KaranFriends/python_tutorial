from sys import stdin, stdout

tt=int(stdin.readline())
while tt>0:
    tt -= 1
    u = stdin.readline()
    li = stdin.readline().replace(" ","")
    # print(li)
    li=li[:-1]
    li = li.lstrip('0')
    li = li.rstrip('0')
    # print(li,"len", len(li))
    l,r=0,0
    flag=0
    if li.count("1") == 1:
        print("YES")
        continue
    while len(li)!=1:
        # print("length   ",len(li))
        # print("asdasdasd", li)
        li=li[1:]
        r=li.find("1")
        # print(li)
        # print("l     ",l,"      r",r)
        if(r>=5):
            li=li[r:]
        else:
            flag=1
            break

    if flag==0:
        print("YES")
    else:
        print("NO")
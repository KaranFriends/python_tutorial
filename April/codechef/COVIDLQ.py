from sys import stdin, stdout

tt=int(stdin.readline())
while True:
    tt -= 1
    # u = stdin.readline()
    li = stdin.readline()
        # .replace(" ","")
    # print(li)
    li=li.strip("0")
    # print(li)
    l,r=0,0
    flag=0
    if li.count("1") == 1:
        print("YES")
        continue
    while len(li)!=2:
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
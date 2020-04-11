tt = int(input())
er = []
u = 1
while tt >0:
    tt-=1
    t = int(input())
    arr=[]

    for i in range(t):
        e=input()
        arr.append([e.strip("*"),len(e.strip("*"))])

    arr = sorted(arr,key=lambda arr : arr[1])
    last = arr[-1][0]
    flag = True
    for j in range(arr[-1][-1]):
        temp = arr[-1][0][-1]
        for i in range(t):
            if arr[i][0] != "":
                if arr[i][0][-1] == temp:
                    arr[i][0] = arr[i][0][:-1]
                    continue
                else :
                    flag = False
                    # print("*")
                    break
            else:
                continue
        # print(arr[-1][0][-1])
        if arr[-1][0] == "":
            break
        if flag == False:
            break
        # print(arr)
    if flag == True:
        er.append("Case #%d: " % (u) + last)
        # print(last)
    else:
        er.append("Case #%d: " % (u) + "*")
        # print("*")
    u+=1

for i in er:
    print(i)
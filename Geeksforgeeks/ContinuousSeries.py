t = int(input())
while t>0:
    t-=1
    size = int(input())
    arr = list(map(int,input().rstrip().split()))
    if size == 1:
        print(0)
        continue
    count = 0
    pre = arr[0]
    flag = False
    e = 1
    if (arr[0] < arr[1]) and (arr[0] + 1 == arr[1]):
        pre = arr[1] + e
        flag = True
        e += 1
    else:
        pre = arr[1] + e
        flag = False

        # e

    if size == 2 and flag == True:
        print("1")
        continue
    for i in range(2,len(arr)):
        if flag == True:
            if pre == arr[i]:
                if pre - e -1 < arr[i]:
                    pre = arr[i] + e
                    e += 1
                else:
                    count += 1
                    e = 1
                    pre = arr[i] + e
                    flag = False
                    e += 1
            else:
                count += 1
                e = 1
                pre = arr[i] + e
                flag = False
                e += 1
        elif flag == False:
            if pre != arr[i]:
                e=1
                pre = arr[i] + e
                e+=1
            elif pre == arr[i]:
                if pre - e -1 < arr[i]:
                    pre = arr[i] + e
                    e += 1
                    flag = True
                elif pre - e -1 >= arr[i]:
                    e = 1
                    pre = arr[i] + e
                    e += 1

    print(count)
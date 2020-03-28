from sys import stdin, stdout

def freq(str,k,x):
    print(str, k , x)
    # break the string into list of words
    str = list(str)
    str2 = []
    print(str)
    # loop till string values present in list str
    # for i in str:

        # # checking for the duplicacy
        # if i not in str2:
        #     # insert value in str2
        #     str2.append(i)

    for i in str:
        print(i, str2.count(i)+1, str2)
        if (str2.count(i) + 1) <= x:
            str2.append(i)
        else:
            if k==0:
                print(str2)
                return len(set(str2))
            else:
                k-=1
                str2.append(i)


t = int(stdin.readline())
while t > 0:
    t -= 1
    str = stdin.readline()
    k, x = stdin.readline().split()
    k = int(k)
    x = int(x)
    print(freq(str, k, x))
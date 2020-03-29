# cook your dish here
from sys import stdin, stdout

def freq(str,k,x):
    str = list(str.rstrip())
    # print(str)
    str2 = [0]*26
    ans=0
    for i in range(str.__len__()):
        temp=ord(str[i]) - ord("a")
        # print(temp)
        str2[temp]+=1
        if str2[temp] > x:
            # print("test")
            if k>0:
                k-=1
                str2[temp]-=1
            else:
                print(ans)
                return 0
        else:
            ans+=1

    print(ans)
    return 0


def main():
    t = int(stdin.readline())
    while t > 0:
        t -= 1
        str = stdin.readline()
        k, x = stdin.readline().split()
        freq(str, int(k), int(x))



if __name__ == "__main__":
    main()

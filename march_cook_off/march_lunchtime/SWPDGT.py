from sys import stdin, stdout

t=int(stdin.readline())
while t>0:
    t-=1
    a,b=stdin.readline().split()
    a=int(a)
    b=int(b)

    a2=a%10
    a1=int(a/10)
    b2=b%10
    b1=int(b/10)

    if b1==0 or a1==0:
        if b1==0 and a1==0:
            print(a+b)
            continue
        elif a1==0 and b1!=0:
            print(max((a2*10 + b2)+b1,a+b))
            continue
        elif a1!=0 and b1==0:
            print(max((b2 * 10 + a2) + a1, a + b))
            continue
    else:
        A=b1*10 + a1
        B=b2*10 + a2
        AA=a1*10 + b1
        BB=a2*10 + b2
        print(max(A+B,AA+BB,a+b))
t=int(input())
while t>0:
    t-=1
    a,b=input().split()
    a=int(a)
    b=int(b)

    a2=a%10
    a1=int(a/10)
    b2=b%10
    b1=int(b/10)

    A=b1*10 + a1
    B=b2*10 + a2

    AA=a1*10 + b1
    BB=a2*10 + b2

    print(max(A+B,AA+BB,a+b))
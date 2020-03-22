from sys import stdin, stdout
t = int(input())

# type(t)
while t > 0:
    n=int(stdin.readline())
    m = stdin.readline()
    m=list(m.rstrip())
    # ans=[]
    print(m)
    for i in m:
        if m.index(i)==(m.__len__()-1):
            break
        print(m[m.index(i)],  m[m.index(i)+1])
        if m[m.index(i)] == m[int(m.index(i))+1]:
            m=m[:int(m.index(i))+1]+m[int(m.index(i))+2:]
            #m.remove(i)
            print("duplicate removed")

        if i=="L" and m[m.index(i)+1] =="R":
            m.remove(m[m.index(i)+1])
            print("R removed")
        elif i=="R" and m[m.index(i)+1] =="L":
            m.remove(m[m.index(i)+1])
            print("L removed")
        elif i=="U" and m[m.index(i)+1] =="D":
            m.remove(m[m.index(i)+1])
            print("D removed")
        elif i == "D" and m[m.index(i) + 1] == "U":
            m.remove(m[m.index(i) + 1])
            print("U removed")
    x,y=0,0
    for i in m:
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
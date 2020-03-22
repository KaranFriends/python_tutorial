from sys import stdin, stdout
t = int(input())

# type(t)
while t > 0:
    n=int(stdin.readline())
    m = stdin.readline().split("")
    ans=[]

    for i in m:
        if m.index(i)==(m.__len__()-1):
            break
        if m[m.index(i)] == m[m.index(i)+1]:
            m.remove(i)

        if i=="L" and m[m.index(i)+1] =="R":
            m.remove(m[m.index(i)+1])
        elif i=="R" and m[m.index(i)+1] =="L":
            m.remove(m[m.index(i)+1])
        elif i=="U" and m[m.index(i)+1] =="D":
            m.remove(m[m.index(i)+1])
        elif i == "D" and m[m.index(i) + 1] == "U":
            m.remove(m[m.index(i) + 1])
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
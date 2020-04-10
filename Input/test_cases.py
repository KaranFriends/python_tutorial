import random

li = []
for i in range(-1000,1001):
    li.append(i)
e = 100
file1 = open("/home/karan/input.txt","a")
while e>0:
    e-=1
    a = []
    for i in range(9):
        a.append(random.choice(li))
    random.shuffle(a)
    file1.write("\n"+str(a) )

file1.close()
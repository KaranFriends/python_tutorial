from sys import stdin,stdout
t = int(stdin.readline().rstrip())

def some_function(e):
    try:
        # print(e.index("gfg"))
        e.index("gfg")
        return True
    except:
        return False

while t > 0:
    t -= 1
    e1=stdin.readline().rstrip()
    ans=0
    while True:
        # print(e1)
        if some_function(e1):
            e1.index("gfg")
            ans+=1
            # print(e1)
            e1=e1[e1.index("gfg")+3:]
            # print(e1)
        else:
            break

    print(ans) if ans > 0 else print("-1")

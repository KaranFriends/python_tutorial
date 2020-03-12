def main():
    from sys import stdin, stdout


    t=int(stdin.readline())
    pair=[(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8)]
    points = [(2,2),(1,3),(3,1),(4,2),(5,1),(1,5),(2,6),(1,7),(7,1),(8,2),(2,8),(3,7),(4,8),(8,4),(7,5),(8,6),(6,8),(7,7),(8,8)]
    while t > 0:
        steps=0
        count=19
        step=[]
        e=stdin.readline().split()
        r,c=int(e[0]),int(e[1])
        orr,occ =r,c
        for i in pair:
            # print(i[0]+i[1])
            if (r,c) == i :
                steps+=1
                step.append((1,1))
                r,c=1,1
                break
            elif r+c == i[0]+i[1]:
                steps+=2
                step.append((i[0],i[1]))
                step.append((1,1))
                r,c=1,1
                break
        if (orr,occ) == (8,8):
            print(steps + 18)
            for i in step:
                print(i[0].__str__() + " " + i[1].__str__())
            for i in points[:-1]:
                print(i[0].__str__() + " " + i[1].__str__())
        else:
            print(steps+19)
            for i in step:
                print(i[0].__str__()+" "+i[1].__str__())
            for i in points:
                print(i[0].__str__()+" "+i[1].__str__())

        t-=1

if __name__ == "__main__":
    main()
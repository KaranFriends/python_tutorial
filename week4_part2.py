
#    [(2, 1),(3, 0)]

def listtodic(ll):
    dic={}
    for i in ll:
        dic[i[0]] = i[1]
    return(dic)


def addpoly(d1,d2):
    for i in d1:
        # print("old"+i.__str__())
        d1[d1.index(i)] = tuple(reversed(i))
        # print("new"+i.__str__())
        # i=i.reverse()
    for i in d2:
        d2[d2.index(i)] = tuple(reversed(i))
        # i=i.reverse()

    d1 = listtodic(d1)
    d2 = listtodic(d2)

    for k,v in d2.items():
        if k in d1.keys():
        # if d1.__contains__(i[0]):
            d1[k] = d1[k] + v
        else:
            d1[k]=v
    


    return(print(d1.__str__()))



addpoly([(4,3),(3,0)],[(-4,3),(2,1)])



# def multpoly():


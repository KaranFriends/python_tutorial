e = input()
inp=[]
while e != "EndOfInput":
    inp.append(e)
    e=input()

books = []
borrowers = []
checkout = []

bok = inp.index('Books')
bor = inp.index('Borrowers')
che = inp.index('Checkouts')

books = inp[bok+1:bor]
borrowers = inp[bor+1:che]
checkout = inp[che+1:]

for i in books:
    books[books.index(i)] = tuple(i.split('~'))

for i in borrowers:
    borrowers[borrowers.index(i)] = tuple(i.split('~'))

for i in checkout:
    checkout[checkout.index(i)] = tuple(i.split('~'))

# print(checkout)
# print(checkout[0][2])

ans = []
e=[]
for i in checkout:
    e.append(i[2])
    for item in borrowers:
        if item[0] == i[0]:
            e.append(item[1])
    for item in books:
        if item[0] == i[1]:
            e.append(item[0])
            e.append(item[1])
    ans.append(e)
    e=[]

# print(ans)
ann ={}

for i in ans:
    if i[0] in ann.keys():
        if i[1] in ann[i[0]].keys():
            if i[2] in ann[i[0]][i[1]].keys():
                ann[i[0]][i[1]][i[2]].append(i[3])
            else:
                ann[i[0]][i[1]][i[2]] = i[3:]
        else:
            ann[i[0]][i[1]] = {i[2]: i[3:]}
    else:
        ann[i[0]] = {i[1]: {i[2] : i[3:]}}

# print(ann)

for i in sorted (ann) :
    for j in sorted(ann[i]):
        for k in sorted(ann[i][j]):
            for l in sorted(ann[i][j][k]):
                print(i+"~"+j+"~"+k+"~"+l)
#            print(i+"~"+ann[i].__str__()+"~"+ann[i][j].__str__()+"~"+ann[i][j][k].__str__())


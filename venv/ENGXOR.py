import atexit, io, sys

# A stream implementation using an in-memory bytes
# buffer. It inherits BufferedIOBase.
buffer = io.BytesIO()
sys.stdout = buffer


# print via here
@atexit.register
def write():
    sys.__stdout__.write(buffer.getvalue())


#####################################
# template ends

# normal method followed
# input N
# n = int(raw_input())

# input the array

def countOne(n):
    ones = 0
    # print(n)
    while n > 0:
        ones = ones + int(n%2)
        n = n/2
    # print(ones)
    return ones


t = int(input())

while t > 0:
    m, n=input().split()
    m=int(m)
    n=int(n)
    f = [int(x) for x in input().split()]
    # f = list(map(int, input().strip().split()))[:m]
    while n > 0:
        odd = 0
        even = 0
        p=int(input())
        for i in f:
            if countOne(i+(p*(i+p))) % 2 == 0 :
                even+=1
            else:
                odd+=1
        print(even.__str__()+" "+odd.__str__())
        n-=1
    t-=1
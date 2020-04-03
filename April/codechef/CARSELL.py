from queue import PriorityQueue
from sys import stdin, stdout

tt=int(stdin.readline())
while tt>0:
    # print(t)
    tt-=1
    q=PriorityQueue()
    t = int(stdin.readline())
    li = stdin.readline().rsplit()
    for i in range(t):
        q.put(-int(li[i]))
    temp=0
    ans=0
    for i in range(t):
        e=-q.get()-temp
        if e<=0:
            continue
        else:
            ans=ans+e
        temp+=1
    print(ans%(10**9+7))
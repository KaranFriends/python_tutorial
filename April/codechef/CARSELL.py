from queue import PriorityQueue
from sys import stdin, stdout

t=int(stdin.readline())
while t>0:
    t-=1
    q=PriorityQueue()
    t = int(stdin.readline())
    map(lambda x: q.put(-int(x)),stdin.readline().rsplit())
    # heapq.heapify(p)
    print(q.get())
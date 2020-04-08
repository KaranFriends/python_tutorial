
def some_funcction(track, e):
    try:
        track.index(e)
        return True
    except:
        return False


class Solution:
    def isHappy(self, n: int) -> bool:
        track =[]
        while True:
            if some_funcction(track, n):
                return False
            else :
                if n==1:
                    return True
                else:
                    s = [ int(i) for i in str(n)]
                    n=0
                    for i in s:
                       n += i*i
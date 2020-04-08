class Solution:
    def isHappy(self,n: int) -> bool:
        track =[]
        while True:
            print(n)
            if track.count(n) > 1:
                return False
            else :
                if n==1:
                    return True
                else:
                    s = [ int(i) for i in str(n)]
                    n=0
                    for i in s:
                        n += i*i
                    track.append(n)

sol = Solution
sol.isHappy(input())